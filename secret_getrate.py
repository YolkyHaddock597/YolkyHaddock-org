import secrets

def gen_new_token():
    key = secrets.token_urlsafe(120)
    return key