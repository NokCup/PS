n, k = map(int, input().split())
arr = []
count = 0
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for money in arr:
    count += k // money         
    k %= money

print(count)
