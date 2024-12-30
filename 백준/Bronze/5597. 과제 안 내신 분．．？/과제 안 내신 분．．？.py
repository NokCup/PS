# 1부터 30까지의 데이터 정보
data = []
for i in range(1, 31):
    data.append(i)

# 입력한 수를 데이터에서 제거
for _ in range(28):
    data.remove(int(input()))

# 데이터 출력
print(*data, sep='\n')
