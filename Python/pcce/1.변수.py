#변수 : 변수의 할당
#변수에 어떤 값을 저장하는 것 / 단 값을 직접 저장하지는 않고, "참조"를 저장한다.
x=10
y=x

print(f'x={x}')
print(f'y={y}')

del x
#print(f'x={x}')

#None은 아무것도 들어있지 않다를 의미
x=None 
#y변수에 새로운 값을 재할당
y=3
print(f'x={x}')
print(f'y={y}')

#다중변수 할당
x,y=10,20
print(f'x={x}')
print(f'y={y}')

#좌변과 우변의 개수가 다른 경우
#x,y=1,2,3
print(f'x={x}')
print(f'y={y}')
#좌변이 하나인 경우에만 정상 동작 (여러 값을 동시에 저장) // 일종의 튜플
x=1,2,3
print(f'x={x}')
#변수를 교차로 쓰면 서로 교체 가능 // swap

#다중 할당이 불가능한 경우 Swap 구현
x=10
y=30

temp=x
x=y
y=temp

print(f'x={x}')
print(f'y={y}')

