def calculate_coins(sum):
    COINS = [100, 50, 20, 10, 5, 2, 1]
    sum *= 100
    change = {}
    for coin in COINS:
        change[coin] = 0
    for coin in COINS:
        while sum - coin >= 0:
            sum -= coin
            change[coin] += 1

    return change

