# Chapter03-2
# 파이썬 문자형
# 문자형 중요

# 문자형 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 문자형의 길이

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

# 이스케이프 문자 사용
"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""
# I'm Girl

print("I'm Girl")
print('I\'m Girl') #작은 따옴표를 쓸 때 역슬레쉬 사용
print('a \t b') #tab키 만큼 띄어쓰기
print('a \n b') #줄바꿈
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

# 탭, 줄 바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"

print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test' #무조건 따옴표 앞에 r을 붙인다
#escape문을 사용하지 않기 위해 raw string으로 변수 선언
print(raw_s)
print()

# 멀티라인 입력
# 역슬래시 사용
multi_str = \
'''
string
Multi Line
Test
'''
#긴 문장을 보기 쉽게 정리해줌
print(multi_str)

# 문자열 연산
str_o1 = "Python" #문자 하나하나가 리스트라고 생각하면 된다
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Daejeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

# 문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수(upper, isalnum, startwith, count, endswith, isalpha ...)

print("Capitalize: ", str_o1.capitalize())
print("endswith?: ", str_o2.endswith("s")) #마지막 글자가 무엇인지 체크할때 확인
print("replace", str_o1.replace("thon", ' Good'))
print("sorted: ", sorted(str_o1)) #순서 정령해서 리스트 형태로 반환
print("split ", str_o4.split(' ')) #특정 단어나 문장을 분리할때

# 반복(시퀀스)
im_str = "Good Girl!"

print(dir(im_str)) #__iter__ 라는 것이 있다면 반복문이 가능

# 출력
for i in im_str:
    print(i)

# 슬라이싱
str_s1 = "Nice Pyhon"

# 슬라이싱 연습
print(str_s1[0:3]) #3-1까지 나오기 때문에 0 1 2 에 대한 것이 나옴
print(str_s1[5:]) #[5:11]와 같음
print(str_s1[:len(str_s1)]) #str_s1[:11]와 같음
print(str_s1[:len(str_s1)-1]) #str_s1[:10]
print(str_s1[1:4:2]) #1 2 3 에 대해 두칸씩 건너서 출력
print(str_s1[1:9:2]) #1 2 3 4 5 6 7 8 에 대해 두칸씩 건너서 출력
print(str_s1[-5:]) #뒤에서 5번째부터
print(str_s1[1:-2]) #1부터 뒤에서 2번째 전 까지
print(str_s1[::2]) #처음부터 끝까지 두칸 간격으로 출력
print(str_s1[::-1]) #처음부터 끝까지 가져오는데 역으로 출력

# 아스키 코드(또는 유니코드)
a = 'z'
print(ord(a)) #a에 해당하는 아스키코드 값을 알려줌
print(chr(122)) #아스키코드 값을 알파벳 문자로 알려줌
