from .client import send_request

def get_price(symbol):
    path = f"/api/v2/spot/market/tickers?symbol={symbol}"
    res = send_request("GET", path)
    return float(res["data"][0]["lastPr"])
