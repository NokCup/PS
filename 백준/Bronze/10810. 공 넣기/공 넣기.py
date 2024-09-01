n, m = map(int, input().split())        # N = 바구니 개수 M = 반복 횟수
array = [0] * n                         # N개의 0으로 리스트 초기화         ex) [0, 0, 0, 0, 0]

for _ in range(m):
    i, j, k = map(int, input().split())     #i = 시작, j = 끝,   k = 넣을 공의 번호           

    for x in range(j - (i - 1)):           #ex) 1 2 3 =>  1부터 2까지 (2번 반복) 
        array[i + (x - 1)] = k                   # 인덱스 0부터 1까지 k를 넣겠다     
        
print(*array)                            # 리스트 내부 요소를 풀어서 출력
