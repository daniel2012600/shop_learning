import jwt
import time

def make_token(data):
    key = "895BC687BB08374C1963CFA2DEEF1F7E60A75B76DB4F4FF4D5AA2C2A3BF78891"
    now = time.time()
    expiretime = 60 * 60
    payload = {
        "username": data.username,
        "expire": now + expiretime
    }
    return jwt.encode(payload,key,algorithm = 'HS256')
