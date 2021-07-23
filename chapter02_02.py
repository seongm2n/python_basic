# Chapter02-2
# 파이썬 완전 기초
# 파이썬 변수

# 기본 선언
n = 700

# 출력
print(n)
print(type(n))

# 동시 선언
x = y = z = 700
print(x, y, z)
print()

#  선언
var = 75
# 재선언
var = "Change Value"

# 출력
print(var)
print(type(var))

#  Object References
#  변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

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

m = 400
print(m, n)
print(type(m), type(n))
print()

# id(identity) 확인: 객체의 고유값 확인
