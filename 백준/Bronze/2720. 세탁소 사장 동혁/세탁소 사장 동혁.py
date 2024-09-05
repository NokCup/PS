t = int(input())
coins = [25, 10, 5, 1]

for _ in range(t):
    coin_list = []
    c = int(input())
    
    for coin in coins:
        coin_list.append(c // coin)
        c %= coin

    print(*coin_list)

