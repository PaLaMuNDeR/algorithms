"""
Cash register
Minimize the amount of coins you are returning to a client at a cash register. Assume you have coins of denomination: [25, 10, 5, 1].
How would you modify it, if you don't have the coins of 5 cents.

"""

def num_coins(cents):
    coins = [25,10,1]
    num_of_coins = 0
    current_min = 25
    change = {}

    for coin in coins:
        change[coin] = cents % coin

    print change

    while cents > 0:
        best_coin = 1
        biggest_change = 0

        for ch in change.keys():
            if ch > biggest_change and change[ch] < current_min:
                current_min = change[ch]
                best_coin = ch
                print best_coin
            if ch > 1 and change[ch] > biggest_change:
                biggest_change = change[ch]

        num_of_coins += cents / best_coin
        cents = cents % best_coin
        change.pop(best_coin)

    return num_of_coins

# print num_coins(31)
print num_coins(70)