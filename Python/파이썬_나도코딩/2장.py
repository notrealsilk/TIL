#2장

#숫자형 자료
print(5)
print(-10) #음수
print(3.14) #실수
print(1000)

#연산
print(5+3) #덧셈 (+)
print(2*8) #곱셈 (*)
print(3*(3+1))

#문자형 자료
print('풍선') #''안의 글자 그대로 출력
print("나비") #""안의 글자 그대로 출력
print("ㅋ"*9) #문자열과 정수를 섞어 출력

#참과 거짓(boolean 자료)
print(5>10) #False
print(5<10) #True
print(True) #True
print(False) #False
print(not True) #False
print(not False) #True
print(not (5>10))#True

#변수 : 어떤 값을 저장하는 공간

#애완동물을 소개해주세요

name="물"
animal="강아지"
age=4
hobby="산책"
is_adult=age>=3 #참과 거짓


print("우리집" +animal+ "의 이름은" +name+ "이에요.")
 #+대신 ,도 사용 가능..대신 ,사이에 띄어쓰기가 됨

hobby="공놀이" #위에 선언한 hoddy가 여기부턴 공놀이로 변경
print(name+"은" +str(age)+ "살이고," +hobby+ "을 좋아해요") #str..정수형->문자형으로
print(name, "은" ,age, "살이고," ,hobby, "을 좋아해요") #str 없이 바로 변수인 age 사용가능
print(name+"은 어른일까요?" +str(is_adult)) #결과값 : True

#주석 처리

'''작은 따옴표 3개로 가능'''
'''컨트롤,/를 동시에 누르면 여러 문장 주석 가능, 다시 컨트롤,/하면 주석 취소'''

#2장 퀴즈
'''변수명 : station / 변수값 : "사당", "신도림","인천공항" 순서로 입력
/xx행 열차가 들어오고 있습니다.를 출력하기'''

station="사당"
print(station+"행 열차가 들어오고 있습니다.")
station="신도림"
print(station+"행 열차가 들어오고 있습니다.")
station="인천공항"
print(station+"행 열차가 들어오고 있습니다.")