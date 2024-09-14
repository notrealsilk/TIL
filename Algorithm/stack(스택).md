# 스택 (Stack)

## 스택의 특성

: 마지막에 삽입한 자료를 먼저 꺼냄 **(Last In First Out) LIFO구조**

: 배열 사용 가능

- `top` : 스택에서 마지막 삽입된 원소의 위치
- `pop`...pop() /  `push`..append()와 동일

### push

- push 스택구현
    
    - `size` : 스택의 사이즈를 정해줌 (정해줘야 함)
    - `if`문 쪽은 디버깅 부분..

### pop

- pop 스택구현
    - `underflow : top에 뭔가 없다.`

### 파이썬으로 스택 구현 (총괄)

```python
STACK_SIZE = 10
stack = [0]*STACK_SIZE
top = -1

top += 1
stack[top] = 1 # push(1)
top += 1
stack[top] = 2 # push(2)
top += 1
stack[top] = 3 # push(3)

top = -1 # pop() # 출력하기 전에 top을 -1하고 출력하기
print(stack[top+1])
```

## 스택 응용 (괄호 검사)

### 괄호 검사

- 여는 괄호는 `push` / 닫는 괄호는 `pop` 해서 비교
- 스택에 여는 괄호가 남아있으면  >> 오류
- 스택이 비어있는데 닫는 괄호가 나옴 >> 오류 (underflow)

### Function call

프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리

- 가장 마지막 호출된 함수 > 먼저 실행완료, 복귀는 후입선출
