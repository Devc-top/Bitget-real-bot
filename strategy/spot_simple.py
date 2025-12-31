from bitget.spot import get_price

ENTRY_PRICE = None

def should_buy(price):
    global ENTRY_PRICE
    if ENTRY_PRICE is None:
        ENTRY_PRICE = price
        return False
    return price < ENTRY_PRICE * 0.995  # buy dip

def should_sell(price):
    return price > ENTRY_PRICE * 1.01  # take profit
