from flask import request, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from service import auth
from service import clock_punch_api

app_info = Info(title="Clock Punch BFF", version="1.0.0")
app = OpenAPI(__name__, info=app_info)
app.config["JSON_AS_ASCII"] = False
app.config["JSONIFY_MIMETYPE"] = "application/json; charset=utf-8"
CORS(app)

account_tag = Tag(name="Auth", description="User external auth")
tag = Tag(name="BFF", description="BFF for User's Clock Punch Flows")

if __name__ == "__main__":
    app.run(debug=True)

@app.get("/registry/account/clock-punches", tags=[tag])
def get_clock_punches():
    """
    Retrieves clock punches. Supports filtering by date.
    """
    token = request.headers.get("x-user-token")
    username = request.headers.get("x-user-name")
    params = request.args
    response = clock_punch_api.get_clock_punches(token, username, params)
    return jsonify(response.json()), response.status_code

@app.post("/registry/account/clock-punches", tags=[tag])
def post_clock_punch():
    """
    Register a clock punch
    """
    token = request.headers.get("x-user-token")
    username = request.headers.get("x-user-name")
    response = clock_punch_api.register_clock_punch(token, username)
    return jsonify(response.json()), response.status_code

@app.delete("/registry/account/clock-punches", tags=[tag])
def delete_clock_punch():
    """
    Deletes a clock punch registry
    """
    token = request.headers.get("x-user-token")
    clock_punch_id = request.headers.get("x-clock-punch-id")
    response = clock_punch_api.delete_clock_punch(token, clock_punch_id)
    return jsonify(response.json()), response.status_code

@app.post("/account/login", tags=[account_tag])
def login():
    """
    Retrieves an access_token from the external service
    """
    form = request.get_json()
    username = form["username"]
    password= form["password"]
    response = auth.login(username, password)
    return jsonify(response.json()), response.status_code

@app.put("/account/refresh-token", tags=[account_tag])
def refresh_current_token():
    """
    Refreshes user token at the external service
    """
    refresh_token = request.headers.get("x-user-refresh-token")
    response = auth.refresh_token(refresh_token)
    return jsonify(response.json()), response.status_code
