n = int(input())

for i in range(-n + 1, n):      # -2, -1, 0, 1, 2
    print(' ' * abs(i) + '*' * (n - abs(i)))