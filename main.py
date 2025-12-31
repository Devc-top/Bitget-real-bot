from bitget.spot import get_price, place_limit_order
from strategy.spot_simple import *
from config.settings import *
import time

print("🚀 Bitget REAL Spot Bot (Safe Mode)")

while True:
    price = get_price(SYMBOL)
    print("📈 Price:", price)

    size = round(ORDER_USDT / price, 6)

    if should_buy(price):
        print("🟢 BUY signal")
        if not DRY_RUN:
            res = place_limit_order(SYMBOL, "buy", size, price)
            print("ORDER:", res)
        on_buy(price)

    if should_sell(price):
        print("🔴 SELL signal")
        if not DRY_RUN:
            res = place_limit_order(SYMBOL, "sell", size, price)
            print("ORDER:", res)
        on_sell()

    time.sleep(10)
