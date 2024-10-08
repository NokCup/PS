import sys

input = sys.stdin.readline()

for i in input:
    if i in 'abcdefghijklnmopqrstuvwxyz':
        if ord(i) + 13 > 122:
            print(chr(ord(i) - 13), end='')
        else:
            print(chr(ord(i) + 13), end='')
    
    elif i in 'ABCDEFGHIJKLNMOPQRSTUVWXYZ':
        if ord(i) + 13 > 90:
            print(chr(ord(i) - 13), end='')
        else:
            print(chr(ord(i) + 13), end='')
    
    else:
        print(i, end='')