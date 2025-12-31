import hmac
import base64
import time
import hashlib

def get_timestamp():
    return str(int(time.time() * 1000))

def sign(timestamp, method, request_path, body, secret):
    message = f"{timestamp}{method}{request_path}{body}"
    mac = hmac.new(secret.encode(), message.encode(), hashlib.sha256)
    return base64.b64encode(mac.digest()).decode()
  
