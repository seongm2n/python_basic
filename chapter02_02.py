# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700     # 변수 n

# 출력
print(n)
print(type(n))  #n에 대한 자료형을 보여줌 , 700은 정수형이라는 타입을 알려주는 것

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

#  선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)      # 다시 선언했을 때 문자열이므로
print(type(var))    # 자료형도 바뀜
print()

#  Object References
#  변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300)) #int라는 것이 object, 클래스 형태로 내부적으로 300이라는 것을 int형의 값으로 생성 콘솔로 출력
print()

#  예2)
# n -> 777
n = 777

print(n, type(n))
print()

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))
print()

m = 400 # 400재할당
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인: 객체의 고유값 확인

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()

# 다양한 변수 선언
# Camel Case : numberOfCollegeGraduates -> 메소드 선언
# Pascal Case : NumberOfCollegeGraduates -> 클래스 선언
# Snake Case : number_of_college_gradustes -> 파이썬 변수 선언

# 허용하는 변수 선언 법
age = 1
Change =2
aGe = 3
AGE = 4
a_g_e= 5
_age = 6
age_ = 7
_AGE_ = 8
# 1AGE = 7 --> 에러

# 예약어는 변수명으로 불가능 -> 쓰게 되면 에러
# for = 3
# class = 3
"""

False    def       if          raise
None     del       import      return
True     elif      in          try
and      else      is          while
as       except    with        lambda
assert   finally   nonlocal    yield
break    for       note        class
from     or        continue    global
pass

"""
