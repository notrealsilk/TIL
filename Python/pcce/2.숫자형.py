# 숫자 (Number)
# 정수형, 실수형, 복수형
# 정수형은 다른 언어와 달리 값의 범위가 무한함

print("정수형")
x=10
print(f'x={x}')
y=-2000
print(f'y={y}')

# 정수형 값은 범위가 무제한
#import sys
#sys.set_int_max_str_digits(9999999)
#x=9999**9999
#print(x)

#대부분의 다른 언어의 범위는 2^31-1 또는 2^63-1

#정확한 0 값이 존재한다
x=0
print(f'x={x}')

print("실수")
#실수의 0은 정확한 0일까?
x=0.0
print(f'x={x}')

0==0.0 #정수 0가 실수 0이 같은지를 판별하는 연산자 / 파이썬만 같다고 취급
#True..즉, 0.0은 정수 0과 완전히 같은 값으로 친다. (상식정도)

# 실수의 자릿수 표현방법
x=1.45
y=1_000 #1,000
z=142e03 #142*10^3 / 과학표기법

#특수한 실수값
x=float('nan') #not a number의 약자 / 계산이 잘못 되었을 때 사용
y=float('inf') #무한대 / 무한대는 연산(+-)등이 되지않음
z=float('-inf')#-무한대

#복소수형 숫자
x=3+2j #실수부가 3이고, 허수부가 2인 복소수
#y=4+8i #i로는 허수부 표현이 안된다.
print(f'x={x}')
