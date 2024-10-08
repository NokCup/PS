# PS 하며 배운 것 정리

### 인덱싱과 슬라이싱
***

아래 코드에서 인덱싱을 할 때, 정해진 인덱스 값을 넣으면 당연히 ***`IndexError' 가 나온다***. <Br>
하지만, 슬라이싱에서는 정해진 인덱스 값을 초과해도 ***'IndexError' 가 나오지 않는다***.

```py
a = '01234567'

#인덱싱
print(a[7])    # 7   
print(a[8])    # IndexError

#슬라이싱
print(a[:7 + 1])    #01234567
print(a[:999]       #01234567

#슬라이싱2
print(a[-10: 3])  #012
```
<br><br><Br>

### readline() , readlines(), read()
***

`readline()` 
- 한 줄만 입력을 받음
- '\n' 가 포함된다. <br>

```py

import sys
a = sys.stdin.readline()    #Hello World

print(a)
print(list(a))
```
> Hello World<br>
['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '\n']<br>

<br><br><br>

`readlines()`
- 여러 줄을 입력 받고 각 줄이 리스트의 요소가 됨
- EOF에 도달할 때 까지 모든 줄을 입력 받음
- readline() 과 마찬가지로 '\n'가 포함됨

```py
'''
[입력]
Hi        
My name is
N
^Z
'''
import sys

a = sys.stdin.readlines()
print(a)
```

>['Hi\n', 'My name is\n', 'N\n']

<br><br><Br>

`read()`
- 여러 줄을 한번에 문자열로 읽음
- EOF에 도달할 때 까지 모든 줄을 입력 받음
- '\n' 포함됨

```py
import sys

input = sys.stdin.read()
print(input)

input
```
> Hello<Br>
My name<br>
Is

<br><br><br>


