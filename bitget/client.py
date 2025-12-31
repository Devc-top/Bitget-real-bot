import requests
from .auth import get_timestamp, sign
from config.settings import *

def send_request(method, path, body=""):
    timestamp = get_timestamp()
    signature = sign(timestamp, method, path, body, BITGET_SECRET)

    headers = {
        "ACCESS-KEY": BITGET_API_KEY,
        "ACCESS-SIGN": signature,
        "ACCESS-TIMESTAMP": timestamp,
        "ACCESS-PASSPHRASE": BITGET_PASSPHRASE,
        "Content-Type": "application/json"
    }

    url = BASE_URL + path
    r = requests.request(method, url, headers=headers, data=body)
    return r.json()
