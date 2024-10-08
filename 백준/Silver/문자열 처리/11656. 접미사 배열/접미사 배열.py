a = input()

result = []
sorting = []
for i in range(len(a)):
    result.append(a[i:len(a)])
    
sorting = sorted(result)
print(*sorting, sep='\n')
