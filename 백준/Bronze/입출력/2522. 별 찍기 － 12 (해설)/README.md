# [Bronze III] 별 찍기 - 12 - 2522 

[문제 링크](https://www.acmicpc.net/problem/2522) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현

### 제출 일자

2024년 9월 27일 16:44:14

### 문제 설명

<p>예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.</p>

### 입력 

 <p><span class="s1">첫째</span> <span class="s1">줄에</span> N(1 ≤ N ≤ 100)<span class="s1">이</span> <span class="s1">주어진다</span>.</p>

### 출력 

 <p>첫째<span class="s1"> </span>줄부터<span class="s1"> 2×N-1</span>번째<span class="s1"> </span>줄까지<span class="s1"> </span>차례대로<span class="s1"> </span>별을<span class="s1"> </span>출력한다<span class="s1">.</span></p>


<br>

### 문제 해설
***
```py
# 'O' 는 공백을 의미한다.

# n = 1
*

# n = 2
O*
*O*

# n = 3
OO*
O*O*
*O*O*
```
<br> 

위에서 n의 값이 커질수록 행이 늘어나고 있다. 따라서 아래와 같이 반복문을 쓸 수 있다.<br>
> for i in range(1, n + 1)

<br>
n = 3 일때, 행 앞의 공백이 1행부터 3행까지 2,1, 0 으로 줄어든다.<Br> 

<br>

행 앞 공백 이후 나오는 별과 공백을 하나로 묶어주면 다음과 같다.

```py
# n = 3
OO*
O[*O]*
[*O][*O]*
```
즉 '*O' 를 하나로 묶어주면 1행부터 3행까지 0, 1, 2 로 증가하는 것을 알 수 있다. 맨 뒤에 나오는 별은 따로 출력하도록 작성하면 최종적으로 코드는 다음과 같다.<br>

```py
n = int(input(0))

for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * (i - 1) + '*' )
```
