# Chapter03-5
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (JSON)
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name': 'kim', 'phone' : '01033337777', 'birth' : '870514'} #키와 벨류로 이루어져있다.
b = {0: 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 27,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 27),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(               #명시적 선언
    Name='Niceman',
    City='Seoul',
    Age=33,
    Grade='A',
    Status='True'
)

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

#출력
# print('a - ', a['name1']) #키가 존재x -> 에러, name1이라는 것은 없다고 함
print('a - ', a.get('name1')) # get으로 접근할 때 키가 존재x -> none 처리, 더 안정적
print('b - ', b[0])
print('b - ', b.get(0))
print('f - ', f.get('City'))
print('f - ', f.get('Age'))

# 딕셔너리 추가
a['address'] = 'seoul' #동적으로 값을 추가 가능
print('a - ', a)
a['rank'] = [1,2,3]
print('a - ', a)

# 딕셔너리 길이
print('a - ', len(a)) #len -> 키의 갯수 세기
print('b - ', len(b))
print('c - ', len(c))
print('d - ', len(d))

# dict_key, dict_value, dict_items : 반복문(__iter__)에서 사용 가능

print('a - ', a.keys()) #keys -> 키값들만 출력
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())

print('a - ', list(a.keys())) # list 안에 키값만 출력
print('b - ', list(b.keys()))

print()

print('a - ', a.values())
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values())) # list 안에 키값만 출력
print('b - ', list(b.values()))

print()

print('a - ', a.items()) #튜플형태로 그대로 값을 반환
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items())) # list 안에 키값만 출력
print('b - ', list(b.items()))

print()

print('a - ', a.pop('name')) #pop -> 값을 꺼내고 삭제
print('a - ', a)

print('a - ', c.pop('arr'))
print('a - ', c)

print()

print('f - ', f.popitem()) # 무작위로 꺼내서 삭제
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)
print('f - ', f.popitem())
print('f - ', f)

print()

print('a - ', 'birth' in a) #키를 조회할 때 존재하면 참, 존재하지 않으면 거짓
print('b - ', 'city' in d)

# 수정
a['test'] = 'test_dict'
print('a - ', a)
a['address'] = 'dj'
print('a - ', a)

a.update(birth = '910904') #명시적으로 다른 리스트를 넣어서 키값을 수정할 수 있다
print('a - ', a)
temp = {'address' : 'Busan'}

a.update(temp)
print('a - ', a  )
