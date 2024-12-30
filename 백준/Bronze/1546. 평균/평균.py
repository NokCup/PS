n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
sum = 0

for i in scores:
    sum += (i/max_score) * 100
print(sum / n)