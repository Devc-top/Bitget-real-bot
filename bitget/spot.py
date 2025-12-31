from .client import send_request

def get_price(symbol):
    path = f"/api/v2/spot/market/tickers?symbol={symbol}"
    res = send_request("GET", path)
    return float(res["data"][0]["lastPr"])

import json
from .client import send_request

def place_limit_order(symbol, side, size, price):
    body = json.dumps({
        "symbol": symbol,
        "side": side,           # buy / sell
        "orderType": "limit",
        "price": str(price),
        "size": str(size),
        "force": "gtc"
    })
    return send_request("POST", "/api/v2/spot/trade/place-order", body)
    
