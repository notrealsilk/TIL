# 함수

# a,b를 입력받아, a+b를 반환하는 함수
def add(a,b):
    return a+b

print(add(10,5))

# x라는 리스트를 입력받아, 모든 값을 더해서 반환하는 함수
def list_sum(x):
    total = 0
    for i in x :
        total += i
    return total

print(list_sum([1,2,3,4,5,6]))

