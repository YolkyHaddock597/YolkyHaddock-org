import requests
from requests import Session
from requests.exceptions import HTTPError
import json


def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except HTTPError as e:
        # raise detailed error message
        raise HTTPError(e, request_object.text)

class FireBaseInit:
    """ Initailizes Firebase """
    def __init__(self, info, config):
        self.info = info
        self.config = config
        self.requests = requests.Session()
        self.api_key = info["apiKey"]
        self.credentials = None

    def auth(self):
        return Auth(self.api_key, self.requests, self.credentials)

    
class Auth:
    """ Authentication Service """
    def __init__(self, api_key, requests, credentials):
        self.api_key = api_key
        self.current_user = None
        self.requests = requests
        self.credentials = credentials

    def sign_in_with_email_and_password(self, email, password):
        request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}".format(self.api_key)
        headers = {"content-type": "application/json; charset=UTF-8"}
        data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
        request_object = requests.post(request_ref, headers=headers, data=data)
        raise_detailed_error(request_object)
        self.current_user = request_object.json()
        return request_object.json()
    
info = {
    
}

config = None

firebase = FireBaseInit(info, config)

auth = firebase.auth()
try:
    val = auth.sign_in_with_email_and_password("loganmx10@gmail.com", "hj")

except:
    print("incorect login or password")
