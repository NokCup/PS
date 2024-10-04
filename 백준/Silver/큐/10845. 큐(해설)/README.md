# [Silver IV] 큐 - 10845 

[문제 링크](https://www.acmicpc.net/problem/10845) 

### 성능 요약

메모리: 34072 KB, 시간: 60 ms

### 분류

자료 구조, 큐

### 제출 일자

2024년 10월 2일 17:17:06

### 문제 설명

<p>정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.</p>

<p>명령은 총 여섯 가지이다.</p>

<ul>
	<li>push X: 정수 X를 큐에 넣는 연산이다.</li>
	<li>pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>size: 큐에 들어있는 정수의 개수를 출력한다.</li>
	<li>empty: 큐가 비어있으면 1, 아니면 0을 출력한다.</li>
	<li>front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
	<li>back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.</li>
</ul>

### 입력 

 <p>첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.</p>

### 출력 

 <p>출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.</p>

<Br><br>
### 문제 해석
***

파이썬에서 큐를 구현할 때 collections 모듈의 deque() 메서드를 사용한다. 

deque는 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이고, queue 라이브러리를 이용하는 것보다 더 간단하다.

<br>

[첫 코드]
```py
from collections import deque

queue = deque()

t = int(input())
for _ in range(t):
    cmd = input()

    if 'push' in cmd:
        queue.append(cmd[5:])
    
    elif cmd == 'pop':
        if len(queue) == 0:
            print(-1)
            continue
        a = queue.popleft()         
        print(a)
    
    elif cmd == 'size':
        print(len(queue))
    
    elif cmd == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd == 'front':
        if len(queue) == 0:
            print(-1)
            continue
        a = queue[0]
        print(a)
    
    elif cmd == 'back':
        if len(queue) == 0:
            print(-1)
            continue
        a = queue[-1]
        print(a)
```

문제를 풀기 위해 위와 같은 코드를 짜보니 문제점이 있었다.

1. 시간 초과

2. 가독성이 떨어짐.

<br>

시간 초과의 경우에는
`sys 모듈` 의 `sys.stdin.read()` 를 사용하여 한꺼번에 입력받은 후 마지막에 일괄 출력하여 시간을 줄일 수 있었다.

<Br>

이후 코드의 안정성을 높이고, 코드를 간결하게 다시 짰다.

<Br>

```py
from collections import deque
import sys


def q():
    #sys 를 이용해 수행시간을 줄일 수 있다
    input = sys.stdin.read()

    # 공백을 기준으로 쪼개 리스트화
    data = input.splitlines()
    queue = deque()

    #첫번째 줄은 명령어의 개수
    t = int(data[0])
    result = []

    for i in range(1, t + 1):
        cmd = data[i].split()
        
        # push x 
        if cmd[0] == 'push':
            queue.append(cmd[1])
        # pop
        elif cmd[0] == 'pop':
            result.append(queue.popleft() if queue else -1)
        # size
        elif cmd[0] == 'size':
            resu것
***

1. if와 else를 한 줄로 줄일 수 있다. <br>
`A if 조건 else B` : A는 참, B는 거짓 (조건에 리스트가 들어가면 리스트 안에 요소가 있다면 참, 요소가 없다면 거짓이 된다.)


<br>

1. `join()` 함수는 리스트의 요소(문자열)을 연결시켜주는 메서드다.<br> 여기서 중요한 건 문자열을 연결시킨다는 것이다. 리스트 내부의 요소가 정수나 실수와 같은 숫자이면 안된다.



```py
a = [1, 2, 3, 4]    # (variable) a: list[int]

print('\n'.join(a))
```
>[실행 결과]<br>
TypeError: sequence item 0: expected str instance, int found


<Br><br>

map( ) 함수는 리스트의 각 요소를 문자열로 만든다.<br>
이를 이용하면 join( )를 사용할 수 있게 된다.

```py
a = [1, 2, 3, 4]    # (variable) a: list[int]

print('\n'.join(map(str, a)))
```
> [실행 결과]<br>
> 1<br>
2<br>
3<br>
4

