

bid_values = {}
make_bids = True

while make_bids:
    name = input("What is your name ? : ")
    bid = int(input("What is your bidding price ? $ : "))
    bid_values[bid] = name

    more_bids = input("Type 'yes' if there are more people who want to bid, else type 'no'. : ")
    make_bids = True if more_bids=="yes" else False

max_bid = max(bid_values)
print(f"The maximum bidder was {bid_values[max_bid]} with a bid value of ${max_bid}.")