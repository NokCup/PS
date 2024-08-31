a1 = int(input())
a2 = int(input())

print(a1 * (a2 % 10), a1 * ((a2 % 100) // 10), a1 * (a2 // 100), a1 * a2, sep="\n")
