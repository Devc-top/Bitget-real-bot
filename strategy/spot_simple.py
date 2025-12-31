ENTRY_PRICE = None
IN_POSITION = False

def should_buy(price):
    global ENTRY_PRICE, IN_POSITION
    if not IN_POSITION:
        ENTRY_PRICE = price
        return True
    return False

def should_sell(price):
    global IN_POSITION
    if IN_POSITION and price > ENTRY_PRICE * 1.01:
        return True
    return False

def on_buy(price):
    global IN_POSITION
    IN_POSITION = True

def on_sell():
    global IN_POSITION
    IN_POSITION = False
