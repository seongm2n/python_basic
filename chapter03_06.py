# Chapter03-6
# 집합(Set) 특징
# 집합(Set) 자료형(순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4, 4, 4]) #중복x 출력했을때 하나만 출력
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'} # 리스트를 나열하듯이 선언해주어도 집합이다.
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a, 2 in a) # in연산자 사용가능
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)

print('l - ', l)
print('l2 - ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))
print(len(f))

# 집합 자료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 1. 교집합
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2)) # 교집합을 함수로 표현

# 2. 합집합
print('s | s2 : ', s1 | s2)
print('s | s2 : ', s1.union(s2)) # 합집합을 함수로 표현

# 3. 차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2)) # 차집합을 함수로 표현

# 중복 원소 확인
print('s1 & s2 : ', s1.isdisjoint(s2))

# 부분 집합 확인
print('subset : ', s1.issubset(s2)) #s1이 s2의 부분집합이냐?
print('superset : ', s1.issuperset(s2)) #s1은 s2의 값을 전부 포함하느냐?

# 추가 & 제거
s1 = set([1, 2, 3, 4])

# 1. 추가
s1.add(5)
print('s1 - ', s1)

# 2. 제거
s1. remove(2)
print('s1 - ', s1)
# s1. remove(7) 존재하는 수 중에 삭제 가능, 오류발생

s1.discard(3)
print('s1 - ', s1)
s1.discard(7) # 오류 발생 안함
print('s1 - ', s1)

s1.clear() # 전부다 제거
print('s1 - ', s1)

a = [1, 2, 3]
a.clear()
print(a)
