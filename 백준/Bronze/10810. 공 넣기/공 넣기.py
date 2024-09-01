n, m = map(int, input().split())        # N = 바구니 개수 M = 반복 횟수
array = [0] * n                         # N개의 0으로 리스트 초기화 [0, 0, 0, 0, 0]

for _ in range(m):
    i, j, k = map(int, input().split())     #i = 시작, j = 끝, k = 넣을 공의 번호           1 2 

    for x in range(j - (i - 1)):           #  2 ~ 4 3번 반복 : 4 - 2 + 1 = 3 : 0 1 2 /   1 2 2번 반복 : 2 - 1 + 1 : 0, 1
        array[i + (x - 1)] = k
        
print(*array)