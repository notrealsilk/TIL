# Memoization

이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 실행속도 줄임 (동적 계획법의 핵심)

```python
# memo를 위한 배열을 할당, 모두 0으로 초기화
# memo[0]을 0으로, memo[1]는 1로 초기화한다.

def fibo1(n):
global memo
# memo[n] == 0.. fibo(n)이 계산된 적이 없으면
if n >= 2 and memo[n] == 0 :
  memo[n] = fibo1(n-1) + fibo1(n-2) # 저장
return memo[n]

memo = [0]*n+1
memo[0] = 0
memo[1] = 1
```

# DP(dynamic programming)

### **동적계획 알고리즘**

- 최적화 문제를 해결
- 입력 크기가 작은 문제를 모두 해결하고,  그 해를 이용해서 큰 크기의 문제 해결

## 피보나치 수의 동적 계획 알고리즘 적용

다만, 오히려 dp를 쓰면 메모리가 커질 수 도 있기에 사용할 수 있는 경우에 사용

```python
def fibo2(n):
f[0] = 0
f[1] = 1
for i in range(2, n+1):
  f[i] = f[i-1]+f[i-2]
  
return f[n]
```

- 메모이제이션과 DP 관계
  
  ```python
  ## 메모이제이션과 DP의 관계
  
  ### 1. 메모이제이션 (Memoization)
  
  - 정의: 이전에 계산한 결과를 저장하고 재사용하는 최적화 기법
  - 특징:
    - 주로 재귀 함수에서 사용됨
    - Top-down 방식으로 구현 (큰 문제에서 작은 문제로)
    - 필요한 부분만 계산 (Lazy Evaluation)
  - 장점: 
    - 구현이 직관적이고 간단함
    - 필요한 부분만 계산하므로 불필요한 계산 회피 가능
  - 단점:
    - 재귀 호출로 인한 오버헤드 발생 가능
    - 스택 오버플로우 위험
  
  ### 2. 동적 계획법 (Dynamic Programming, DP)
  
  - 정의: 복잡한 문제를 간단한 하위 문제로 나누어 해결하는 알고리즘 설계 기법
  - 특징:
    - 반복문을 사용하여 구현하는 경우가 많음
    - Bottom-up 방식으로 구현 (작은 문제에서 큰 문제로)
    - 모든 부분 문제를 한 번씩 계산
  - 장점
    - 반복문 사용으로 재귀 호출 오버헤드 없음
    - 모든 부분 문제를 순차적으로 해결하여 안정적
  - 단점
    - 때로는 불필요한 부분까지 계산할 수 있음
    - 구현이 메모이제이션보다 복잡할 수 있음
  
  ### 3. 관계
  
  - 메모이제이션은 DP를 구현하는 한 가지 방법
  - DP는 메모이제이션을 포함하는 더 넓은 개념
  - 둘 다 중복 계산을 피하고 효율성을 높이는 것이 목표
  
  ### 4. 예시: 피보나치 수열
  
  메모이제이션 (Top-down):
  
  ```python
  def fib(n, memo={}):
      if n in memo:
          return memo[n]
      if n <= 1:
          return n
      memo[n] = fib(n-1, memo) + fib(n-2, memo)
      return memo[n]
  ```
  
  DP (Bottom-up):
  
  ```python
  def fib(n):
      if n <= 1:
          return n
      dp = [0] * (n+1)
      dp[1] = 1
      for i in range(2, n+1):
          dp[i] = dp[i-1] + dp[i-2]
      return dp[n]
  ```
  
  두 방법 모두 중복 계산을 피하고 효율성을 높이는 데 사용되지만, 접근 방식과 구현 방법에서 차이가 있습니다.
  
  ```
