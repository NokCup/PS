import sys
input = sys.stdin.read  # input 호출 시 전체 입력을 한 번에 불러온다    sys.stdin.read 는 대량의 입력을 한 번에 처리할 때 유용하다.

def main():
    # 공백을 기준으로 리스트 화 시키는데, sys.stdin.read 를 사용했으므로 줄바꿈(공백처리인듯)을 해도 계속 입력이 들어간다.
    data = input().split()
    n = int(data[0])
    k = int(data[1])
    coins = list(map(int, data[2: n + 2]))    # coins은 총 n개(12개) coins 수를 n개(10개) 로 맞추려먼 (2 ~ 12) 로 해야한다. 
     
    coins.sort(reverse=True)        #정렬 후 역순
    
    count = 0    
    for coin in coins:              # '가장 큰 화폐' 순으로 돈을 나눈다.
        count += k // coin
        k %= coin

    print(count)

# 모듈파일과 메인파일이 있다고 가정하고, 메인파일은 모듈을 불러와 모듈에서 정의된 함수들을 사용한다.
# 여기서 메인파일의 이름은 즉 __name__ = "__main__" 이고 모듈은 __name__ = "모듈이름" 이다.

if __name__ == "__main__":
    main()
