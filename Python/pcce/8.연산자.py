#산술연산자
#사칙연산을 포함한 수학적으로 사용되는 연산자

print(14+3) #덧셈은 숫자를 더한다 #17
print([1,2]+[3,4])# 덧셈은 리스트/튜플/문자열을 이어붙인다 #[1, 2, 3, 4]
print(7-16.0) # 뺄셈은 숫자를 뺸다. 정수와 실수를 계산하면 실수가 된다. # -9.0
print(5*20.0) #곱셈은 숫자를 곱한다. # 100.0
print('abc'*12) #곱셈은 리스트/튜플/문지열을 반복한다. # abcabcabcabcabcabcabcabcabcabcabcabc
print(18/6) #나눗셈은 기본적으로 실수를 출력한다 # 3.0
print(18//6) # 정수나눗셈은 //로 표기한다. # 3
print(18//10) # 정수나눗셈은 '몫'을 계산한다. 즉, 소수점 아래는 버린다 # 1
print(18%10) # Modulus 연산은 '나머지'를 계산한다. # 8
print(2**10) # **은 거듭제곱을 의미 #1024
print(-10) # - 는 음의 부호를 의미하는 단항 연산자이다 # -10
print(--10) # - 연산자이기 때문에 두개 연달아 붙이면 양수가 됨 # 10
print(+10) # +는 양의 부호를 의미하는 단항 연산자이다 (의미 x) # 10

# c언어 기반의 언어의 경우
#x=10
#print(--x) # 9
# print(x) # 9

#비교연산자
# 두 값을 비교해서 True/ False를 반환

x=10
y=20
print(x==y) # 두 값이 같으면 T, 다르면 F # False
print(x!=y) # 두 값이 같으면 T, 다르면 F # True
print(x<y) # 앞의 값이 더 작으면 T (less than)
print(x<=y) # 앞의 값이 작거나 같으면 T (less than or equal to)
print(x>y) # 앞의 값이 크거나 같으면 T (Greater tnan)
print(x>=y) # 앞의 값이 크거나 같으면 T (Greater tnan or equal to)

#할당 연산자
#변수에 값을 할당하는 연산자 / 좌측에 변수를, 우측에 값을 놓는다

x=20 # 변수 x에 20이라는 값을 할당
x+=20 # x=x+20을 줄여 쓴 할당 연산자
print(f'x={x}') #40 #{} 안에는 표현식(결정된 값이여야 함)이나 변수가 들어가야함
x-=10 # x=x-10을 줄여 쓴 할당 연산자
print(f'x={x}') # 30
#*, /, //, %, ** 전부 가능

#논리연산자
#논리값으로(T/F)로 연산하는 연산자
print(True and True) #True

x = 30
y =15
print(x >10 and y > 20) #False
print(x >10 or y > 20) #True
print (not(x>10 and y>20)) # True
print (0< x <= 30) #0 < x and x < 30을 줄여 쓴 것 /파이썬만 가능 # True

# 멤버 연산자 (중요)
# 좌측의 값이 우측에 속해 있는지 반환하는 연산자
#True/False로 반환

a = [1,3,5,7,9] #리스트, 튜플, 문자열, 집합, 딕셔너리 가능
print(3 in a) #3이 a에 들어 있으면 T
b= {1:10, 2:30, 3:50} #딕셔너리인 경우 key만 검사
print(1 in b) # 1이 b의 key로 o # T 
print(10 in b) # 1이 b의 key로 x # F
print(10 not in b) # not (10 in b) 랑 같은 의미 # T

#식별연산자
# 두 피연산자가 동일한 객체(메모리살에 있는 자료)를 가리키는지 검사
# 값만 값은게 아니라, 실제 같은 객체여야함

x=[1,2,3,4]
y=x # y는 x와 같은 객체
z=x[:] # z와 x는 다른 객체 - 슬라이싱 과정에서 새 리스트를 만들어준다
print(x is y) # 같은 객체이므로 T
print(y is z) # 다른 객체이므로 F
print(y is not z) # 다른 객체이므로 T

