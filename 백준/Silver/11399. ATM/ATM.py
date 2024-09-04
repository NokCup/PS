import sys
input = sys.stdin.read

def main():
    people = input().split()
    person = int(people[0])
    min = list(map(int, people[1: person + 1]))
    
    min.sort()  # 정렬 1, 2, 3, 3, 4

    plus = 0
    array = []
    for i in min:
        plus += i
        array.append(plus)

    print(sum(array))

if __name__ == "__main__":
    main()