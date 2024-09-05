import sys

t = int(input())        
timer = [500, 60, 10]

count = []
for time in timer:

    if t % 10 != 0:
        print(-1)
        sys.exit()
    counter = 0
    counter += t // time        
    t %= time
    
    count.append(counter)

print(*count)
