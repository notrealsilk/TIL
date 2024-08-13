## 좋은 알고리즘?
- 정확도 / 작업량 / 메모리 사용량 / 단순성 / 최적성

## 시간복잡도

- 실제 걸리는 시간 측정
- n에 대한 항만 표시 (계수 제외)

----------------------
# 배열 = list

자료형의 변수들을 하나의 이름을 열거하여 사용하는 자료구조

배열을 하면 변수들이 실제 메모리에도 순서대로 들어감

## 1차원 배열

- 1차원 배열
    
    `Arr = [0] * 10`..배열 선언
    
    : 배열을 사용할 때는, 크기를 미리 정해주는 것이 좋음 (`append()`는 느려서 지양)
    
    `Arr[idx] = 20` ..배열 접근하는 법
    
    : 배열 Arr의 `idx`번 원소에 20을 저장하라
    
    # 정렬
    
    오름차순, 내림차순
    
    ## 버블 정렬 (Bubble sort)

    
    인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식 / O(n**2)
    
    - 기준 인덱스가 있어야 함
    - [0], [1] / [1], [2] / [2], [3]… 형식으로 비교
    - 진행되면서 기준 인덱스 범위가 하나 씩 줌 (n-1)
    
    : [0] ~ [n-1] /  [0] ~ [n-2]….
    
    
    ```python
    N = 5
    arr = [55, 7, 78, 12, 42]
    
    for i in range(N-1, 0, -1):  # 각 구간의 끝 인덱스 i
        for j in range(i):  # 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
            if arr[j] > arr[j+1]:  # 왼쪽 원소가 더 크면 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(*arr)
    ```
    
    ## 카운팅 정렬 (Counting sort)
    
    
    항목들의 순서를 결정위해 집합에 각 항목이 몇 개씩 있는지 세는 작업
    
    선형 시간에 정렬하는 효율적 알고리즘
    
    - 정수에 적용 가능 / 카운트를 위해 집합 내 가장 큰 정수를 알아야 함
    - 시간복잡도 : O(n+k)
    
    ---
    
  
    
    - 코드
        - 카운팅 정렬1
        
        ```python
        DATA = [0, 4, 1, 3, 1, 2, 4, 1]
        COUNTS = [0] * 5 # DATA가 0~4까지의 정수
        
        N = len(DATA) # DATA의 크기
        TEMP = [0] * N # 정렬 결과 저장
        
        # 1단계 : DATA 원소 별 개수 세기
        for x in DATA: # DATA 원소 x를 가져와서 COUNTS[x]에 개수 기록
            COUNTS[x] += 1
        
        # 2단계 : 각 숫자까지의 누적 개수 구하기
        for i in range(1,5): # COUNT[0]~COUNT[4] 까지 누적 개수
            COUNTS[i] += COUNTS[i-1]
        
        # 3단계 : DATA 맨 뒤부터 TEMP에 자리 잡기
        for i in range(N-1, -1, -1): # N-1~ 0까지
            COUNTS[DATA[i]] -= 1 # 누적개수 1개 감소
            #idx = [COUNTS[DATA[i] # 아래와 같은 경우가 어려우면 이렇게 한단계 거쳐도 ㄱㅊ
            TEMP[COUNTS[DATA[i]]] = DATA[i]
        
        print(*TEMP)
        ```
        
        - 카운팅 정렬2
        
        ```python
        
        def counting_sort(arr, k):
            """
            input_arr : 입력 배열 (0 -> k)
            counting_arr: 카운팅 배열
            k 는 데이터의 개수가 아닌, 데이터 원소 범위 // (0,1,2,3,4)..5개의 범위
            """
            counting_arr = [0] * (k + 1)  # 카운팅 배열  // k 는 데이터의 원소 범위 // [0,0,0,0,0]
        
            # 1. counting_arr 에 input_arr 내 원소의 빈도수 담기
            for i in range(len(arr)):  # input_arr 만큼 순회 // input_arr의 원소 하나씩 꺼내기
                counting_arr[input_arr[i]] += 1  # counting_arr[0], counting_arr[4]
        
            # 2. 누적(counting_arr) 업데이트 -> 내 앞에 몇개 ?
            for i in range(1, len(counting_arr)):
                counting_arr[i] += counting_arr[i - 1]  # counting_arr[1] = counting_arr[1] + counting_arr[0]]
        
            # 3. result_arr 초기화: 정렬된 결과
            result_arr = [-1] * len(arr)
        
            # 4. result_arr에 정렬하기(counting_arr를 참조 할것이다.) [0, 4, 1, 3, 1, 2, 4, 1]
            for i in arr:  # arr 는 순회 가능한 iterable 객체 -> collection
                counting_arr[i] -= 1  # 0, 4, 1, 3 .... : counting_arr의 해당 원소 값 하나 줄인다.
                result_arr[counting_arr[i]] = i # result_arr에 counting_arr의 해당 요소를 넣는다.
        
            return result_arr
        
        input_arr = [0, 4, 1, 3, 1, 2, 4, 1]  # 정렬할 target
        
        print(counting_sort(input_arr, 4)) [0, 1, 1, 1, 2, 3, 4, 4]
        
        ```
        
    
    ### 완전검색
    
    모든 경우의 수 생성하고 테스트
    
    - 완전 검색으로 시작 > 접근법을 도출하여 다른 알고리즘 찾기
    
    ### 순열
    
    
    `arr = [’123’, ‘132’, ‘213’,’231’, ‘312’, ‘321’]`
    
    >> 코드로 만들 수도 있어야하지만, 완전 검색로 arr리스트를 만들어서 할 수 있어야 함
    
    ### 탐욕(Greedy) 알고리즘
    
    최적으로 생각되는 방법을 선택해 나가는 방식으로 최종적인 해답에 도달 (머릿속에 떠오르느 생각을 검증 없이 바로 구현)
    
    - 최적이라는 보장은 없지만 부분적으로 가능
    
    ```python
    #‘44354’ to 리스트
    data = list(map(int,input())
    
    #‘4 4 3 5 4’ to 리스트
    data = list(map(int,input().split())
    ```
    
    ```python
    num = 45678 # baby gin 확인할 6자리수
    c = [0] * 12 # 6자리 수로 부터 각 자리 수를 추출하여 개수를 누적할 리스트
    
    ## 많이 사용하는 방법
    
    for i in range(6):
    c[num % 10] +=1 # 마지막 자리부터 탐색하면서 i를 c[i]에 넣음
    num//=10 # i를 날리고 다음 i+1로 넘어감
    ```

    ---
  ## 2차원 배열

- 2차원 배열
    
    ### 배열 순회
    
    모든 원소를 빠짐없이 조사
    
    - 순회종류 코드(3) // 행,열,지그재그
        
        ### 행 우선 순회
        
        ```python
        for i in range(n): # i행의 좌표
        	for j in range(m): # j행의 좌표
        		f(arrat[i][j]) 
        		
        ```
        
        ### 열 우선 순회
        
        ```python
        for i in range(n): # i행의 좌표
        	for j in range(m): # j행의 좌표
        		f(arrat[j][i]) 
        ```
        
        ### 지그재그 순회
        
        ```python
        for i in range(n): # i행의 좌표
        	for j in range(m): # j행의 좌표
        		f(array[i][j + (m-1-2*j)*(i%2)]) 
        		# m-1을 하면 마지막 열의 인덱스가 나옴
        		
        # i는 증가하는 방향
        # j는 증가, 감소같이 두 방향 존재
        
        # i가 짝수일 경우 >> [j] # 증가
        # >> (i%2) 때문에 i가 짝수이면 (m-1-2*j)*(i%2)가 전부 0이 됨
        
        # i가 홀수일 경우 >> [m-1-2*j] # 감소
        
        ```
        
    
    ### 델타를 이용한 2차 배열 탐색
    
    2차원 배열에서 4방향의 인접 배열 요소를 탐색
    
    ### 전치 행렬
    
    ```python
    arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3행렬
    
    for i in range(3):
    	for j in range(3):
    	# 만약 대각선의 오른쪽이면, 대각선에 있는 값들을 서로 바꿈
    	# 오른쪽이 아닌 경우는 전치 행렬 바꾸는 기준에 어긋남	
    		if i<j:
    		# arr[i][j]<->arr[j][i]..대각선끼리 값 바꾸기
    			arr[i][j], arr[j][i] = arr[j][i], arr[i][j] 
    ```
    

        ```python
        """
        5
        45 15 10 56 23
        96 98 99 40 69
        96 84 49 46 34
        16 64 81 4 11
        10 66 85 55 14
        
        """
        
        N = int(input())
        
        arr = [list(map(int,input().split())) for _ in range(N)]
        
        print(arr)
        # [[45, 15, 10, 56, 23], [96, 98, 99, 40, 69], [96, 84, 49, 46, 34], [16, 64, 81, 4, 11], [10, 66, 85, 55, 14]]
        
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        
        total = 0
        
        for i in range(N):
            for j in range(N): # NxN 배열의 모든 원소에 대해
        
                s = 0 # 문제에서 원소와 주변 인접 원소의 차의 절대값의 합 저장
        
                # i,j 원소의 4방향 원소에 대해
                for k in range(4):
                    ni = i + di[k]
                    nj = i + dj[k]
        
                    if 0<ni<N and 0<=nj<N:
                        s += abs(arr[i][j] - arr[ni][nj]) # 실존하는 인접원소 ni, nj 와의 차의 절대값 abs()
                
                total += s
        
        print(total)
        
        ```
        
    
    ## 부분집합 합
    
    
    ### 비트 연산자
    
    - 비트연산자 / 일단 보류
        - 알고리즘 효율높이기 위해 사용
            

            
        
        ```python
        arr = [3,6,7,1,5,4]
        
        n = len(arr) # n : 원소의 개수
        
        for i in range(1<<n): # 1<<n: 부분집합의 개수
         for j in range(n): # 원소의 수만큼 비트를 비교함
        	 if i & (1<<j): # i의 j번 비트가 1인 경우
        		 print(arr[j], end =",") # j번 원소 출력
        	print()
        print()
        ```
        
    
    # 검색 (Search)
    
    저장돼 있는 자료 중에서 원하는 항목 찾는 작업
    
    ## 순차 검색 (sequential search)
    
    일렬로 돼 있는 자료를 순서대로 검색
    
    - 정렬 X 경우
    
    : 순차적 검색 → 키 값과 동일한 원소, 원소를 인덱스로 반환 → 끝까지 찾지 못하면 검색 실패
    
    ```python
    def search (arr,n,key):
    # arr : 탐색할 리스트 / n : 리스트 길이 / key : 찾아야할 값
    	i = 0
    	# 리스트 인덱스 순으로 순회하면서 key 값 찾기
    	while i < n and arr[i] != key:
    		i = i+1
    		
    	if i < n :
    		return i
    	else :
    		return -1
    ```
    
    - 정렬 O 경우
    
    : 순차적으로 검색 -> 키값을 비교 -> (키 값 > 검색대상 키값), 찾는 원소가 없는 것으로 검색 종료
    
    ```python
    def search (arr,n,key):
    	i = 0 
    	while i < n and arr[i] < key: # 인덱스 검사를 먼저 해야함 (단축평가 때문)
    		i = i+1
    	if i < n and arr[i] == key: 
    		return i
    	else : 
    		return -1
    ```
    
    ```python
    for i in range(0, n-1):
    	if a[i] == key:
    		return i
    	elif a[i] > key :
    		return -1
    	
    	return -1
    ```
    
    ## 이진 검색 (binary search)
    
    자료 가운데 있는 항목의 키 값과 비교하여 다음 검색 위치 결정, 검색 진행
    
    **자료가 “정렬”된 상태여야 함**
    
    - 가운데 값 찾기 : `(start + end) // 2`
    
    ```python
    def search(a, N, key):
        start = 0  # 시작 원소 인덱스
        end = N - 1  # 마지막 원소 인덱스
    
        # 남은 구간이 있으면 while문 순회
        while start <= end:
            mid = (start + end) // 2
            if a[mid] == key:  # 검색 성공
                return True
            elif a[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
                
        return False  # 검색 실패
    
    ```
    
    - 인덱스
    
    : 대량의 데이터를 매번 정렬하면 느리므로, 배열 인덱스를 사용 >> db 인덱스는 **이진 탐색 트리 구조**
    
    ## 해쉬(hash)
    
    다루진 않을 것
    
    # 선택 정렬 (Selection sort)
    
    주어진 자료 중, 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환
    
    - 단점
    
    : 시간복잡도(O(n^2))가 크다
    
    ```python
    def seacch(a,n):
    	for i in range(N-1): # 기준위치 (구간 시작) // 기준위치를 최솟값 위치로 가정
    		min_idx = i
    		for j in range(i+1, N):
            if arr[j] < arr[min_idx]:  # 현재 위치와 비교해서 더 작은 값을 찾으면
               min_idx = j  # 최소값의 위치를 업데이트
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 찾은 최소값을 기준 위치로 이동 
    		
    ```

