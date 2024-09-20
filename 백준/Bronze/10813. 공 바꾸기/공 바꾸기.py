n, m = map(int, input().split())

arr = []
for i in range(1, n + 1):
    arr.append(i)

for _ in range(m):
    i, j = map(int, input().split())
    k = arr[j - 1]
    arr[j - 1] = arr[i - 1]
    arr[i - 1] = k 

print(*arr)


