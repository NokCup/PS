from collections import deque
import sys

input = sys.stdin.read

def main():
    queue = deque()
    data = input().splitlines()  # 모든 입력을 한 번에 읽기
    t = int(data[0])  # 첫 번째 줄은 명령어의 개수

    results = []
    for i in range(1, t + 1):
        cmd = data[i]

        if cmd.startswith('push'):
            queue.append(cmd[5:])  # 'push X'에서 X를 큐에 추가
            
        elif cmd == 'pop':
            if not queue:
                results.append(-1)  # 큐가 비어있을 경우 -1 출력
            else:
                results.append(queue.popleft())  # 가장 앞의 요소를 제거하고 출력
        
        elif cmd == 'size':
            results.append(len(queue))  # 큐의 크기를 출력
        
        elif cmd == 'empty':
            results.append(1 if not queue else 0)  # 큐가 비어있으면 1, 아니면 0 출력
        
        elif cmd == 'front':
            results.append(-1 if not queue else queue[0])  # 큐가 비어있을 경우 -1 출력
        
        elif cmd == 'back':
            results.append(-1 if not queue else queue[-1])  # 큐가 비어있을 경우 -1 출력

    # 결과를 한 번에 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    main()