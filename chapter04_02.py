# Chapter04-2
# 파이썬 반복문
# FOR 실습

# 코딩의 핵심
# for in <collection>
#     <Loop body>

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


for v1 in range(10): # N-1로 생각하기, 0 ~ 9
    print('v1 is : ', v1)

print()

for v2 in range(1, 11): # 1 ~ 10
    print('v2 is : ', v2)

print()

for v3 in range(1, 11, 2): # 1~10 중에 2씩 점프해서 출력
    print('v3 is : ', v3)

print()

# 1 ~ 1000합
sum1 = 0

for v in range(1, 1001):
    sum1 += v # sum = sum + 1

print('1 ~ 1000 sum : ', sum1)

print('1 ~ 1000 sum : ', sum(range(1, 1001)))

print('1 ~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4))) #4의 배수

print()

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Cho1', 'Yoo']

for n in names:
    print('You are : ', n)

print()

# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

print()

# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

print()

# 예제4
my_info = {
    "name": 'Lee',
    "Age": 33,
    "City": "Seoul"
}

# 키만 출력
for key in my_info:
    print('key : ', key)

# 키값 출력
for value in my_info:
    print('value : ', my_info[value]) # == my_info.get(vlaue)

for v in my_info.values():
    print('value : ', v)

print()

# 예제5
name = 'FineAppLE'

for n in name:
    if n.isupper(): #대문자 인지 검사 ,islower -> 소문자인지 검사
        print(n)
    else:
        print(n.upper()) #소문자일 경우 n을 upper함수로

# break

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)

print()

# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    print("current type: ", v , type(v))
    print("multiply by 2", v * 3)
    print(True * 3)

print()

# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 24:
        print("Found : 24!")
        break               # 24를 찾고 break를 시켰기때문에
else:                       # else구문은 출력되지 않는다.
    print('Not Found : 24')

print()

# 구구단 출력
for i in range(2, 10): # 2~9
    for j in range(1,10): # i나오고 j(1~9)실행
        print('{:4d}'.format(i * j), end='') # for문이 끝나고 다음단으로
    print()

print()
# 변환 예제
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2))) # namecA 거꾸로 출력 
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 순서x
