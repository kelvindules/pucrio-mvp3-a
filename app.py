from flask import request, jsonify
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag

from service import auth
from service import clock_punch_api

app_info = Info(title="Clock Punch BFF", version="1.0.0")
app = OpenAPI(__name__, info=app_info)
CORS(app)

account_tag = Tag(name="Auth", description="User external auth")
tag = Tag(name="BFF", description="BFF for User's Clock Punch Flows")

@app.get("/registry/account/clock-punches", tags=[tag])
def get_clock_punches():
    """
    Retrieves clock punches. Supports filtering by date.
    """
    token = request.headers["x-user-token"][0]
    username = request.headers["x-user-name"][0]
    params = request.args
    return jsonify(clock_punch_api.get_clock_punches(token, username, params))

@app.post("/registry/account/clock-punches", tags=[tag])
def post_clock_punch():
    """
    Register a clock punch
    """
    token = request.headers["x-user-token"][0]
    username = request.headers["x-user-name"][0]
    return jsonify(clock_punch_api.register_clock_punch(token, username))

@app.delete("/registry/account/clock-punches", tags=[tag])
def delete_clock_punch():
    """
    Deletes a clock punch registry
    """
    token = request.headers["x-user-token"][0]
    clock_punch_id = request.headers["x-clock-punch-id"][0]
    return jsonify(clock_punch_api.delete_clock_punch(token, clock_punch_id))

@app.post("/account/login", tags=[account_tag])
def login():
    """
    Retrieves an access_token from the external service
    """
    form = request.get_json()
    username = form["username"]
    password= form["password"]
    return jsonify(auth.login(username, password))

@app.put("/account/refresh-token", tags=[account_tag])
def refresh_current_token():
    """
    Refreshes user token at the external service
    """
    refresh_token = request.headers["x-user-refresh-token"][0]
    return auth.refresh_token(refresh_token)
