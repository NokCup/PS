import sys
s = sys.stdin.readlines()

for i in s:
    min_count = 0
    max_count = 0
    num = 0
    blank = 0
    for j in i:
        
        if j in 'abcdefghijklnmopqrstuvwxyz':
            min_count += 1
        elif j in 'ABCDEFGHIJKLNMOPQRSTUVWXYZ':
            max_count += 1
        elif j == ' ':
            blank += 1
        elif j in '1234567890':
            num += 1
        
    print(min_count, max_count, num, blank)



