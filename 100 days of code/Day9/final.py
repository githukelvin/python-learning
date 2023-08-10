import os
import art

print(art.art)
# Clearing the Screen
bids = []
bid_ongoing = True


def place_your_bid():
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What is your bid?: $"))
    bid = {'name': bidder_name, "price": bidder_price}
    bids.append(bid)


def check_winner(arr):
    prices = []
    for bidders in arr:
        prices.append(bidders['price'])
    highest_price = max(prices)
    for bidder in arr:
        if bidder["price"]  == highest_price :
            name = bidder['name']
            msg = f"The winner is {name} with a bid of ${highest_price}"
            print(msg)



is_there_another_bidder = 'yes'

while bid_ongoing:
    if is_there_another_bidder == 'yes':
        place_your_bid()
        is_there_another_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")
        os.system('cls')


    else:
        bid_ongoing = False
        check_winner(arr=bids)
