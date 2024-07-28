# 1번
# 최솟값 구하기 (min함수 제외)
# ---------------------------
def min_score(scores):
    min = scores[0]
    for num in scores:
        if min > num :
            min = num
    return min

'''
1. 함수에서 min_score 리스트를 파라미터로 받은 다음, score[0]을 min 변수에 저장
2. min_score[0]을 기준으로 for문으로 순회하면서 리스트 안에 있는 다른 숫자들과 비교
3. 만약 min>num 이면 min을 num으로 재할당
4. 순회가 끝나면 min을 return
'''
def min_score(target_list):# 저는 항상 def함수 만들때 매개변수이름을 고칩니다. 이유는 받아오는게 무슨 형태인지 까먹지않기위해! 그래서 이번엔 target_list!!!
    int_min_score = target_list[0] #0번째를 기본으로 갖고 0번째와 나머지를 for문으로 전부 비교해서 작으면 int_min_score에 재할당 합니다.
    for i in range(len(target_list)):
        if target_list[i] < int_min_score:
            int_min_score = target_list[i]
    return int_min_score
  '''
  for문에서 반복가능한 객체로 리스트의 길이를 range()로 받아와서 리스트 길이만큼 반복
  인덱싱으로 값을 비교하면서 값이 작으면 int_min_score값을 재할당
  '''
# 기준값을 먼저 정하는 방식은 같음 / for문에서 리스트를 그대로 가져오거나 리스트의 인덱싱을 해서 가져오는 방식의 차이
############### 테스트 코드 ################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 40
#########################################

# 2번
# 60보다 아래인 수 갯수 구하기

def under_60(scores):
    sub_count = 0
    for i in scores:
     if i < 60 :
       sub_count += 1
    return sub_count 

'''
1. 함수 under_60()는 under_60 리스트를 파라미터로 받음
2. 과목 수를 저장할 sub_count 변수를 할당
3. under_60 리스트를 for문으로 순회하면서 60보다 작으면 sub_count 변수에 +=1씩 더한다.
4. 순회가 끝나면 sub_count을 return
'''

def under_60(target_list): #이번에도 받아오는게 리스트 군요. 따라서 target_list
    under_count = 0 #초기화를 해두고
    for i in range(len(target_list)): #target_list 수만큼 반복해서 target_list[i]와 60을 비교합니다.
        if target_list[i] <60: #비교해서 60보다 작으면 아까 0으로 초기화해둔 under_count에 하나씩 추가합니다
            under_count +=1
    return under_count #마자믹에 추가한 under_count를 return해줍니다.

############## 테스트 코드 #################
print(under_60([30, 60, 90, 70])) # 1
print(under_60([0, 10, 20, 30, 40, 50])) # 6
print(under_60([50, 70, 50, 45, 80, 80])) # 3
##########################################

# 3번
# 빈 값이 있으면 False 반환

def is_user_data_valid(user_data):
    if user_data['id'] == '' or user_data['password'] == '':
        return False
    else :
        return True

'''
1. 함수 is_user_data_valid()는 딕셔너리를 파라미터로 받음
2. 딕셔너리의 ['id']와 ['password'](key값의 value를 불러옴)의 value가 ''(입력이 없으면)이면 False 반환
3. 그렇지 않으면 True 반환
'''

def is_user_data_valid(target_user_data): #딕셔너리 user_data를 받았네요.
    try:
        if target_user_data['id'] != '' and target_user_data['password'] != '': 
        #target_user_data['id'] = 딕셔너리id키의 value값/_______/target_user_data['password'] = 딕셔너리password키의 value값
        #5번 줄은 "두가지 Value값이 모두 빈문자열이 아니면" 라는 조건식
            return True
        else:
            return False
    except KeyError: 
        #try/except문으로 KeyError나왔을때를 해결!!! 예를들어 우리가 받는 target_user_data에 키값이 올바르지 않는경우.
        #user_data1 = {'id2': '','passwordAA': '1q2w3e4r'} 다음과같을때 오류를 해결하기 위해서 넣음
        return False

# try-except문을 사용했구나..

############## 테스트 코드 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################


# 4번
# 아이디의 끝자리가 숫자여야 True

def is_id_valid(user_data):
    id_end = user_data['id'][-1] # str도 인덱싱 가능
    if id_end in ['0','1','2','3','4','5','6','7','8','9']: # id_end는 str
        return True
    else :
        return False

'''
1. 함수 is_id_valid()는 딕셔너리를 파라미터로 받음
2. 딕셔너리의 key ['id']의 value의 마지막 값을 id_end 변수에 저장
3. id_end 변수에 저장된 숫자는 문자열(str)형식이므로 숫자가 문자열 형식으로 저장된 리스트와 비교함
4. 0~9 숫자가 있으면 True, 아니먄 False 반환
'''

def is_id_valid(target_data): #target_data로 변경.
    last_id = [0,1,2,3,4,5,6,7,8,9] #id의 마지막이 0부터9라고했으니까. 해당 값을 리스트로 만듬. 왜냐하면! 뒤에 나옴.
    target_data_id = target_data['id'] #받아온 target_data에서 id의 Value값만 가져옴. 비밀번호는 필요없어.

    try:
        if int(target_data_id[-1]) in last_id: 
            #가져온 id의 Value값의 마지막 값을 int(target_data_id[-1]) 이렇게 표현함.
            #int(target_data_id[-1]) 해당값이, 아까 만들어둔 last_id = [0,1,2,3,4,5,6,7,8,9] 안에 포함되는지 확인!!!!
            return True #안에있으면 True!
        else:
            return False #없으면 False!
    except ValueError: 
        #ValueError 하는 이유:
        #user_data1 = {'id': 'jungssafy5AAA','password': '1q2w3e4r'} 다음과같을때. jungssafy5AAA의 A를 int화 못하기 때문에 발생하는 ValueError를 예방하기위해.
        return False


def is_id_valid(user_data):
    user_id = user_data.get('id', '')
    # 아이디가 빈 문자열이 아닌지 확인하고 마지막 문자가 숫자인지 확인합니다.
    if user_id and user_id[-1].isdigit():
        return True
    return False
'''
내가 짠 코드가 타입형 때문에 복잡한 것 같아, 다른 방법을 알아보기위해 챗지피티에서 물어봄
위의 코드는 챗지피티 코드이며, 입력된 문자열이 숫자인지 판별하는 isdigit()메소드를 사용.
'''


############## 테스트 코드 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################

