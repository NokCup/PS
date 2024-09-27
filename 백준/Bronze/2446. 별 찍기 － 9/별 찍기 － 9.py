n = int(input())

for i in range(-n + 1, n):      # -4, -3, -2, -1, 0, 1, 2, 3, 4
    print(' ' * ((n - 1) - abs(i)) + '*' * (2*(abs(i) + 1) - 1))