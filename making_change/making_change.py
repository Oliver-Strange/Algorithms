#!/usr/bin/python

import sys


def making_change(amount, denominations):
    '''
    cache = [0] * (amount + 1)
    cache[0] = 1

    for coin in denominations:
        print(coin)
        for i in range(coin, amount + 1):
            print(i)
            total = i - coin
            cache[i] += cache[total]
    return cache[amount]
    '''
    if amount == 0:
        return 1
    elif (amount < 0 or denominations == []):
        return 0
    elif amount == 2:
        return 1
    else:
        return (making_change(amount, 1) + making_change(amount, 5) + making_change(
            amount, 10) + making_change(amount, 25) + making_change(amount, 50))


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
