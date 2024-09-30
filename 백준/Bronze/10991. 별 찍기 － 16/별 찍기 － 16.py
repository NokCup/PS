n = int(input())

for i in range(1, n + 1):   # 1 2 3
    print(' ' * (n - i) + '* ' * (i - 1) + '*')
