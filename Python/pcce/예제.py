# 2. 아래 리스트 x를 뒤집어 이어 붙이세요.
# 즉, [x[0], x[1], x[2], ... x[n-1], x[n-1], x[n-2], ..., x[1], x[0]] 이 되게 하세요.
x = [0, 1, 2, 3, 4, 5]
y = (x[::-1]) #슬라이싱을 하면 새로운 리스트를 만든다.
print (x+y)

#x.reverse() 는 정방향이 사라짐 (기존 리스트 수정)/ [::-1]을 사용해야함 (새로운 리스트 생성)

# 3. 아래 리스트의 값의 수를 중복을 제외하고 구하세요.
x = [-4, 2, -5, -5, 3, 7, 3, -2, 5, -5, 8]
y = set(x)
print(len(y)) # len(set(x))


# 4. 아래 튜플을 내림차순된 튜플로 변경하세요.
x = (5, 2, 0, 6, 3, 1, 9, 10)
y=list(x)
y.sort(reverse=True)
answer= tuple(y)
print(answer)

#6번
x= 'abcdef'
y='ghijkl'
z=[None] * (len(x)+ len(y))
z[::2] = x
z[1::2] = y
answer = ''.join(z)
print(answer)

#조건문 예제1

country_name = input ('국가명을 입력하세요 :')

if country_name in ['Korea', 'korea']: # 리스트 사용해서 여러 개 중에 일치하는게 있는지 확인
    print('한국입니다.')
elif country_name == 'America' or country_name =='america':
    print('미국입니다.')
elif country_name == 'Japan' or country_name == 'japan' :
    print('일본입니다.')
else:
    print('지원하지 않는 국가입니다')

'''country_name == 'America' or 'america': 
# -> T/F or 'america' 순으로 실행됨.. 그래서 이렇게 쓰면 안됨
or 연산자는 논리 연산자라서 문자열끼리는 비교가 안됨'''

# 조건문 예제2
score = int(input ('점수를 입력하세요 :')) #int를 이용해서 문자열->정수 변환

if score >= 90: 
    print('A')
elif score >= 80: # score < 90 은 이미 내제 ㅇ..굳이 안 써도 ㅇ
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')

# 조건문 예제3

math = int(input ('점수를 입력하세요 :'))
eng = int(input ('점수를 입력하세요 :'))

if math >= 90 : 
    if eng >=90:
        print('Perfect!')
    elif eng >= 40:
        print('수학천재!')
elif eng >=90 :
    if  math >=40:
        print('영어천재!')
elif math >=40:
    if eng >= 40:
        print('과락')
else:
    print('준수함')

#조건문 예제3

#"10,40".split
math, eng = input('수학점수와 영어점수를 띄어쓰기로 구분해서 입력하세요 : ').split(" ")
math = int(math) # 두 변수 사이에 띄어쓰기가 있으므로 정수가 아닌 것이 ㅇ..input에 int 씌울 수 없음
eng = int(eng)

if math < 40 or  eng < 40 : 
    print('과락')
else:
    if  math >=90 or  eng >= 90:
        print('Perfect!')
    elif eng >= 90:
        print('수학천재!')
    elif math >=90:
        print('영어천재!')
    else:
        print ('준수함')

# 반복문 예제1
numbers = input ('숫자를 입력하세요 :').split(" ") #split()..문자열 리스트로 변경
numbers = list(map(int, numbers)) # map()..numbers(각 문자열) 에 각각 int 씌어줌

max_val = ('-inf') # i에 어떤 값이 들어오든 -inf보다 크므로 max_val에 숫자가 들어옴
for i in numbers:
    if max_val < i:
        max_val = i
print(max_val) 

