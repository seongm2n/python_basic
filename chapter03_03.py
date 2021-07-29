# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
# print(len(c)) = 4
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>>>')
print('d - ', type(d), d )
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1]) #역순으로 출력
print('e - ', e[-1][1]) # e 인덱싱 안에 첫번째 리스트 출력
print('e - ', list(e[-1][1]))

#  슬라이싱
print('>>>>>')
print('d - ', d[0:3]) #d의 0 1 2 까지 출력
print('d - ', d[2:])
print('e - ', e[-1][1:3]) # e인덱싱 안에 1 2 리스트 출력

# 리스트 연산
print('>>>>>')
print('c + d', c + d)
print('c * 3', c * 3) # 3번 반복, 순서유지
print("'Test' + c[0]", 'Test' + str(c[0])) # str을 붙여서 형변환을 해준다

# 값 비교
print(c == c[:3] + c[3:]) # c 와 c의 0 1 2 + 마지막 원소 3 더한 것과 같다
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>>>')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] #첫번째 75 인덱싱에 하나의 리스트가 들어감
print('c - ', c)
"""
c[1:2] = [['a', 'b', 'c']]
print('c - ', c)
결과값 => c - [4, ['a', 'b', 'c'], 80, 85]
# 두번째 인덱싱이 하나의 리스트가 된다.
"""
c[1] = ['a', 'b', 'c'] # 괄호 두개 사용하기 싫으면 하는 것
print('c - ', c)
c[1:3] = [] # 두번째 인덱싱을 비우기 => 삭제라고는 할 수 없다.
print('c - ', c)
del c[2] # 삭제
print('c - ', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 마지막 끝에 삽입하고 싶을 때 쓰는 함수
print('a - ', a)
a.sort() # 오름차순으로 정렬
print('a - ', a)
a.reverse() # 들어있는 데이터를 반대로 위치 구조를 바꿔서 출력
print('a - ', a)
print('a - ', a.index(3)) # a의 3번째 인덱스 함수를 출력
print('a - ', a[3]) # a의 3을 가져오라했을 때 위의 것과 출력값이 같음
a.insert(2, 7) #두번째 위치에 7을 넣을 것, 그리고 원래 위치에 있던 애들을 뒤로 싹 밀어버림
print('a - ', a)
a.reverse()
print('a - ', a)

"""
del a[9543] # 만약 만 개가 있는 것에 9543번째를 지우고 싶을 때 숫자가 크니까 버거움
# 인덱스로 제거하는 것은 불가능, 데이터의 갯수가 적을 때는 상관이없다.
print('a - ', a)
"""
a.remove(10) # 불필요한 데이터를 제거하는 함수
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
"""
pop은 마지막에 있는 인덱스 원소를 꺼내오고,
기존에 있는 원소 리스트를 다시 구성해서 출력하는 것
"""
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4)) # 값이 들어있나 안들어있나 확인
print('a - ', a.count('사과'))
ex = [8,9]
a.extend(ex) # a리스트에 ex를 extend함
print('a - ', a)

# 삭제 : remove(내가 원하는 값을 바로 삭제), pop(끝에 있는 값만 제거), del(내가 원하는 인덱스 번호를 알아야 한다는 것)

# 반복문 활용
while a:
    data = a.pop() # 끝부분 원소부터 꺼내서 활용
    print(data)
