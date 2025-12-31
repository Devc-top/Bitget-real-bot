from bitget.spot import get_price
from strategy.spot_simple import should_buy, should_sell
import time

SYMBOL = "BTCUSDT"

print("🚀 Bitget REAL Spot Bot Started")

while True:
    price = get_price(SYMBOL)
    print("Price:", price)

    if should_buy(price):
        print("🟢 BUY signal (REAL)")
        # place_order("buy")  # ENABLE LATER

    if should_sell(price):
        print("🔴 SELL signal (REAL)")
        # place_order("sell")

    time.sleep(5)
