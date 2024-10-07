s = input()
alpha = [-1] * 26

for i in range(len(s)):
    if alpha[ord(s[i]) - 97] == -1:
        alpha[ord(s[i]) - 97] = i
    else:
        continue

print(*alpha)