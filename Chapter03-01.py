# Chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린(참거짓)
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전
"""
# 1. 데이터 타입
str1 = "Python"
bool = True
str2 = 'Anaconda'
float_v = 10.0  #10(정수) == 10.0(실수)
int_v = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}
tuple = (7, 8, 9) # 7,8,9도 가능
set = {3, 5, 7}

# 데이터 타입 출력
print (type(str1))
print (type(bool))
print (type(str2))
print (type(float_v))
print (type(int_v))
print (type(list))
print (type(dict))
print (type(tuple))
print (type(set))

# 2. 숫자형 연산자
"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) x ** y -> 2 ** 3 == pow(2,3) == 8
"""

# 정수 변환
i = 77
i2 = -14
big_int = 7777777777777777700000000000000000000

# 정수 출력
print(i)
print(i2)
print(big_int)

# 실수 출력
f = 0.9999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 39
i2 = 939
big_int1 = 77777777777777777777700000000009999999999
big_int2 = 888888989989809090909302492049049320492049204294
f1 = 1.234
f2 = 3.939

# +
print(">>>>>+")
print("i1 + i2 : ", i1 + i2)
print("f1 + f2 : ", f1 + f2)
print("big_int1 + big_int2 : ",big_int1 + big_int2)

# *
print(">>>>>*")
print("i1 * i2 : ", i1 * i2)
print("f1 * f2 : ", f1 * f2)
print("big_int1 * big_int2 : ",big_int1 * big_int2)

# -
print(">>>>>-")
print("i1 - i2 : ", i1 - i2)
print("f1 - f2 : ", f1 - f2)
print("big_int1 - big_int2 : ",big_int1 - big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

#  타입 출력
print(type(a), type(b), type(c), type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0
print(float(False))

print(complex(3))
print(complex('3')) #문자형 -> 숫자형으로 바꿈
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x, y = divmod(100, 8) #나눈다음 몫x와 나머지y 확인
print(x,y)
print(pow(5,3), 5 ** 3) #5의 세제곱

# 외부 모듈
import math

print(math.ceil(5.1)) # x이상의 수 중에서 가장 작은 정수
print(math.pi) #math에 있는 pi를 가져와서 출력
