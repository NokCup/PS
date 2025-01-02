n, m = map(int, input().split())     
arr = []

for x in range(1, n + 1):
    arr.append(x)

for _ in range(m):
    i, j = map(int, input().split())
    k = arr[i-1 : j]
    k.reverse()
    arr[i-1:j] = k

print(*arr)

