stack = []
t = int(input())
for _ in range(t):
    cmd = input()
    
    if 'push' in cmd:
        stack.append(int(cmd[5:]))

    elif cmd == 'pop':
        if stack == []:
            print(-1)
            continue
        z = stack.pop()
        print(z)

    elif cmd == 'size':
        print(len(stack))

    elif cmd == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)

    elif cmd == 'top':
        if stack == []:
            print(-1)
            continue
        top = stack[-1]
        print(top)

        