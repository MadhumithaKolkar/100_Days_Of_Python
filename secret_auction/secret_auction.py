import art

print(art.logo)
bid_values = {}
make_bids = True

while make_bids:
    name = input("What is your name ? : ")
    bid = int(input("What is your bidding price ? $ : "))
    bid_values[name] = bid

    more_bids = input("Type 'yes' if there are more people who want to bid, else type 'no'. : ")
    make_bids = True if more_bids=="yes" else False

max_bid = float("-inf")
max_bidder = ""

for names,bid in bid_values.items():
    if bid>max_bid:
        max_bid = bid
        max_bidder = names
print(f"The maximum bidder was {max_bidder} with a bid value of ${max_bid}.")