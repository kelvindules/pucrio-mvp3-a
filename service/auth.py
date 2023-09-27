import requests

login_url = "https://api.escuelajs.co/api/v1/auth/login"
refresh_token_url = "https://api.escuelajs.co/api/v1/auth/refresh-token"


def login(username, password):
    return requests.post(login_url, data={"email": username, "password": password})


def refresh_token(token):
    return requests.post(refresh_token_url, data={"refreshToken": token})
