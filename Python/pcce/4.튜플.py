#튜플
#리스트와 비슷한, 여러 개의 자료를 묶는 자료형
#다른 점은 튜플은 불변형 (자료 추가, 수정, 제거 불가)

#튜플 생성
x=tuple() #빈 튜플 생성
print(f'x={x}') # x=()
x=() # 빈 튜플 생성

x=(1,2,3) # x=1,2,3 이라 해도 됨
print(f'x={x}')
x=(5,) #값이 하나뿐인 튜플은 ,를 써줘야 튜플이 됨..괄호 연산자와 혼동되기 때문에
print(f'x={x}')

#튜플에서 제공되는 기능
#x.sort() // 튜플은 불변이므로 정렬 불가능
y=x.count(10) #접근만 하는 것이므로 가능