#문자열

문장='나는 소년입니다.'
print(문장) 

문장2="""
나는 소년이고 파이썬은 쉬워요."""
print(문장2)

#슬라이싱
"""일부 숫자, 문자만 가져오는 것이 슬라이싱"""

주민번호="901211-1234567" #앞 숫자부터 0번째 자리 #주민번호는 '-' 까지 포함해서 13자리 #주민번호=변수

print('성별 : '+주민번호[7]) #문자열 중 필요한 숫자만 가져오고 싶을 때 [] 사용
print('년도 : '+주민번호[0:2]) #0번째 부터 2번째 자리 직전까지.. 즉, 0, 1번째 숫자 가져옴
print('월 : '+주민번호[2:4])
print('일 : '+주민번호[4:6])
print('생년월일 : '+주민번호[:6]) # print('생년월일 : '+주민번호[0:6]) #0번째 부터 6번째 자리 직전까지..
print('뒷자리 : '+주민번호[7:]) #print('뒷자리 : '+주민번호[7:14]) #7번째 자리부터 끝까지

print('뒷자리 (거꾸로) : '+주민번호[-7:]) #맨 뒤에서 7번째 끝까지 #뒷자리는 -1부터 시작

#문자열 처리 함수
python="Python is Amazing"

print(python.lower()) # lower() : 소문자로 바꿈
print(python.upper()) # upper() : 대문자로 바꿈
print(python[0].isupper()) #isupper() : 변수 python의 0번째 문자열이 대문자인가 #True
print(len(python)) #len() : 문자열 길이  #17
print(python.replace("Python", "Java")) #replace() : "Python"->"Java"로 변경
#Java is Amazing

#index

index=python.index("n") #첫번째 알파벳 n이 몇번째 자리에 있는가
print(index) #5

index=python.index("n", index+1) #두번째 알파벳 n이 몇번째 자리에 있는가
print(index) #15

index=(python.find("n")) #find() #첫번째 알파벳 n이 몇번째 자리에 있는가 
print(index) #5

print(python.find("java")) # -1 #find는 값이 없으면 -1 출력 
#print(python.index("java")) # 에러 #index는 값이 없으면에러가 나면서 프로그램 종료)

print(python.count("n")) #count() : n이 몇 번 등장하는가


#문자열 포멧

#방법1 : %

print("나는 %d살 입니다." %20) #나는 20살 입니다. #d는 정수
print("나는 %s을 좋아합니다." %"파이썬") #나는 파이썬을 좋아합니다. #s는 문자열, 즉 str
print("Apple은 %c로 시작해요." %"A") #"Apple은 A로 시작해요. #c는 문자, 즉 한 문자만 받겠다
# %s로 하면 정수, 문자열, 문자 모두 출력 가능

print("나는 %s색과 %s색을 좋아해요."%('파란', '빨간')) #나는 파란색과 빨간색을 좋아해요.

#방법2 : {}, format() 함수

print("나는 {}살 입니다.".format(20))#나는 20살 입니다.
print("나는 {}색과 {}색을 좋아해요.".format('파란', '빨간')) #나는 파란색과 빨간색을 좋아해요.

print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) #나는 빨간색과 파란색을 좋아해요. #format 함수 속 0번째=파란와 1번째=빨간 순서

#방법3

print ('나는 {age}살이고, {color}색을 좋아해요'.format(color='빨간',age=20))
#나는 20살이고 빨간색을 좋아해요.

#방법4 (버전 3.6 이상부터) 

age=20
color='빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요.')
#나는 20살이고 빨간색을 좋아해요.

#탈출문자

#\n : 줄바꿈
print('벡문이 불여일견\n백견이 불여일타')
'''벡문이 불여일견
   백견이 불여일타'''

#\" \' : 문장 내 따옴표
print('저는 "나도코딩"입니다.')#저는 "나도코딩입니다."

print("저는\"나도코딩\"입니다.")#저는 "나도코딩입니다."

#\\ : 문장 내에서 \

print("python3 \\Users\\Desktop\\파이썬\\3장.py")

#\r : 커서를 맨 앞으로 이동

print("Rad Apple\rPine") #PineApple #(Pine이 앞으로 가는 것)

#\b : 벡스페이스 (힌글자 삭제)
print("Rad Apple\rPine") #RadApple #(Pine이 지워짐)

#\t : 탭
print("Rad Apple\rPine") #Rad   Apple 


#4장 퀴즈

"""사이트 별로 비밀번호를 만들어주는 프로그램 작성"""

"""
예) http://naver.com
규칙1 http:// 부분은 제외하기 > naver.com
규칙2 처음 만나는 점(.) 이후 부분은 제외 > naver
규칙3 남은 글자 중 처음 세자리 + 남은 글자갯수 +글자 내 'e' 갯수 +'!'로 구성

예)생성된 비밀번호 : nav51!"""


"""풀이1"""

url="http://naver.com"


my_str=url.replace ("http://","") #규칙1 (http://을 ""으로 교체)

#print (my_str)=naver.com

my_str= my_str[:my_str.index(".")] # 규칙2
#my_str[0:5] -> 0~5 직전까지, (0,1,2,3,4)

#print (my_str)=naver

password=my_str[:3]+str(len(my_str)) + str(my_str.count('e'))+"!"

print ("{0}의 비밀번호는 {1}입니다.".format(url, password)) #nav51!


"""풀이2"""

url="http://naver.com"

#규칙 1

mystr=url.replace("http://","") #print(mystr)=naver.com


#규칙 2

mystr=mystr[:5] #print(mystr)=naver


#규칙 3

password=mystr[:3]+str(len(mystr))+str(mystr.count("e"))+"!"

print(password) #print(password)=nav51!
