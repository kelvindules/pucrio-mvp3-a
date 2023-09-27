import requests
from requests import Response

clock_api_url = "http://localhost:5001/clock-punches"


def get_clock_punches(token, username, params):
    return requests.get(
        clock_api_url + f"/{username}", params=params, headers={"Authorization": f"Bearer {token}"}
    )

def register_clock_punch(token, username):
    return requests.post(
        clock_api_url, data={"token": token, "username": username}
    )

def delete_clock_punch(token, clock_punch_id):
    return requests.delete(
        clock_api_url + f"/{clock_punch_id}", headers={"Authorization": f"Bearer {token}"}
    )
