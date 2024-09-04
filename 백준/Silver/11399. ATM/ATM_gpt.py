import sys
input = sys.stdin.read

def main():
    people = input().split()              # 사람 수와 인 당 몇 분씩 걸리는지 입력
    person = int(people[0])               # 사람 수
    mins = list(map(int, people[1: person + 1]))  #걸리는 시간
    
    min.sort()  

    current_sum = 0                      # 원래 코드에서는 누적 대기시간을 저장하기 위해 array 리스트를 사용했다. 해당 코드는 리스트를 없애고 메모리 사용을 줄였다.
    total_sum = 0
    for min in mins:
        current_sum += min
        total_sum += current_sum

    print(total_sum)

if __name__ == "__main__":
    main()
