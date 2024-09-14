# 패턴매칭

## 고지식한 알고리즘 (Brute Force)

모든 문자열 순회하면서 패턴 내의 문자들을 일일이 비교하는 방식

- 라이브 수업코드
    
    ```python
    p = "is" #'찾을 패턴'
    t = "This is a book" # 전체 텍스트 길이
    M = len(p) # 찾을 패턴의 길이
    N = len(t) # 전체 텍스트의 길이
    
    i = 0
    j = 0
    while i < N and i < M:
    	if t[i] != p[j]:
    		i = i-j # t 인덱스
    		j = -1 # p 인덱스
    	i = i+1
    	j = j+1
    	
    if j == M : 
    	return i-M # 검색성공
    else :
    	return -1 # 검색실패
    
    ```
    
    ```python
    t = "TTTTTABC"
    P = 'TTA'
    N = len(t)
    M = len(p)
    cnt = 0
    
    for i in range(N-M+1): # 비교 시작위치
        for j in range(M):
            if t[i+j] != p[j]:
                break # for j, 다음 글자부터 비교 시작
            else:
                cnt += 1
    print(cnt)
                
    ```
    
- 고지식한 알고리즘 코드 _자세한 설명
    
    ```python
    ## 고지식한 알고리즘
    
    target = "Hello SSAFY 12th!"  # target 패턴을 찾을 대상
    pattern = "SSA"  # 우리가 찾을 패턴
    
    def BruteForce(pat, text):
        N = len(text)
        M = len(pat)
        i = 0  # text의 인덱스
        j = 0  # 패턴의 인덱스 (M보다 작을 경우까지 탐색)
    
        while j < M and i < N: # 패턴이 일치할 때까지 i, j값 증가시키기
    
            # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
            if text[i] != pat[j]: # 일치하지 않은 곳
                # text의 현재 위치에서 일치하지 않는 곳을 발견! -> i를 증가시켜야 함
                # j값과 일치하는 요소가 i에 나올 때까지 j는 증가시킬 필요가 없음
    
                #  지금위치 - j
                i = i - j # text의 인덱스 i를 현재 실패한 위치로 되돌리는 역할
                # 순회 한 번이 끝나면 무조건 앞으로 나아가야 함
                # 일치하는 값이 나오지 않았다면 j는 제자리에 있어야 하므로 여기서 j에 -1을 해줌
                j = - 1
    
            i = i + 1
            j = j + 1
    
            # 검색 성공
            if j == M:
                return i - M # text에서 패턴이 시작된 인덱스를 반환
            else:
                return -1
    
    # 심플 버전
    text = "This is simple version"
    pattern = 'vision'
    
    def BruteForceV2(pat, text):
        for idx in range(len(text) - len(pat) + 1): # 패턴 길이에 맞게 순회
            # 패턴을 처음부터 끝까지 순회
            for j in range(len(pattern)):
    
                # 1. 다르면, break / 패턴 순회를 돌 필요가 없음
                if text[idx + j] != pat[j]:
                    break
            # 같다면(다른게 없다면)
            else:
                return idx
        # 검색실패
        else:
            return -1 # 외부 for문을 다 돌았다 = 패턴 매칭이 안됐다.
    
    ```
    

## KMP 알고리즘

- 불일치가 발생한 텍스트 스트링의 앞 부분에 어떤 문자가 있는지를 미리 알고 있으므로, 불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행
- 패턴을 전처리하여 배열을 구해서 잘못된 시작을 최소화 (매칭이 실패했을 때 돌아갈 곳을 계산!)
- 코드
    - 시각화
        
        [KMP Simulator](https://cmps-people.ok.ubc.ca/ylucet/DS/KnuthMorrisPratt.html)
        
        [KMP](https://gbhat.com/algorithms/kmp.html)
        
    - LPS 배열 만들기
        
        ```python
        def makeLPS(pattern):
            M = len(pattern)  # 패턴의 길이
        
            LPS = [0] * M # LPS 배열 생성
            same_p_idx = 0 # 동일 패턴 인덱스
            idx = 1 # 패턴체크 인덱스
        
            while idx < M: # M 길이 만큼 체크
                if pattern[same_p_idx] == pattern[idx]: # 같은 패턴을 가지고 있으면
                    same_p_idx += 1 # 같은 패턴 발견해서 1 증가
                    LPS[idx] = same_p_idx # 체크 인덱스 자리에 같은 패턴 갯수 추가
                    idx += 1 # 다음 자리수 확인
                else:  # 패턴이 같지 않다면
                    if same_p_idx != 0: # 현재 동일 패턴이 있으면
                        # AAACAAAA 와 같은 패턴이 있는 경우 
                        # 마지막 AAAA 패턴에서 마지막 A는 4번째 자리인 C와 다름
                        # 그래서 0으로 초기화 하려니 AAA 3개의 동일한 패턴을 가지고 있음
                        # 해당 패턴인 경우라면 이전 same_p 값으로 돌아가서 (그럼 P[same_p] 는 A가 됨)
                        # 현재 비교하려는 chk_idx와 비교하여 동일한 값이므로 패턴갯수가 유지됨
                        same_p_idx = LPS[same_p_idx-1] # 이전 LPS 값으로
                    else:
                        LPS[idx] = 0
                        idx += 1
            return LPS
        ```
        
    - KMP 탐색
        
        ```python
        def KMP(T, P):
        
            lps = makeLPS(T)
        
            # i : text를 순회하는 index
            i = 0
            # j : pattern을 순회하는 index
            j = 0
        
            position = -1
            while i < len(T):
                # 같으면 이동
                if P[j] == T[i]:
                    i += 1
                    j += 1
                else:
                    # 다른데 j가 0이 아니라면, i의 자리는 유지한 채 j만 이동 후 비교 시작
                    if j != 0:
                        j = lps[j - 1]
                    # 다른데 j가 0이라면, i를 한칸만 이동하여 처음부터 진행 하듯이 진행
                    else:
                        i += 1
                # j가 pattern을 다 순회하면 성공
                if j == len(P):
                    position = i - j
                    break
        
            return position
        
        T = 'abcdabeeababcdabcef'
        P = 'eaba'
        
        position = KMP(T, P)
        print(position)
        
        ```
        

(B형)

```python
def kmp(t, p):
    N = len(t)  # 텍스트의 길이
    M = len(p)  # 패턴의 길이
    lps = [0] * M  # LPS 배열 초기화

    # LPS 배열 계산
    length = 0  # 가장 긴 접두사와 접미사의 길이
    i = 1
    
    while i < M:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # LPS 배열을 참조하여 길이 조정
            else:
                lps[i] = 0
                i += 1

    # 패턴 검색
    i = 0  # 텍스트 인덱스
    j = 0  # 패턴 인덱스
    
    while i < N:
        if p[j] == t[i]:
            i += 1
            j += 1
        
        if j == M:  # 패턴이 발견된 경우
            print(i - j, end=' ')  # 패턴의 시작 인덱스 출력
            j = lps[j - 1]  # 다음 비교를 위해 패턴 인덱스 조정
        
        elif i < N and p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]  # 패턴 인덱스 조정
            else:
                i += 1  # 텍스트 인덱스 증가

    print()  # 줄 바꿈
    return

# 예제 사용
t = 'zzzzzabcacfcbca'
p = 'abcacf'
kmp(t, p)

```

## 보이어-무어 알고리즘

- 오른쪽에서 왼쪽으로 비교 /  대부분의 소프트웨어가 채택
- 패턴에 오른쪽 끝에 있는 문자가 불일치하고, 이 문자가 패턴 내에 존재하지 않는 경우, 이동 거리는 무려 패턴의 길이만큼이 됨
    
    
- 코드
    - 시각화
        

        
    - skip table 만들기
        
        ```python
        # T : target / P : pattern
        T = 'abcdabeeababcdabcef'
        P = 'eaba'
        
        def pre_process(T):
            M = len(T)
        
            # skip 배열 대신 딕셔너리
            PI = dict()
        
            # (M - i - 1)만큼 스킵하지만
            # 마지막 index를 제외한 이유 : 마지막 index가 matching이 되었는데 실패했으면 M만큼 skip해야 하기 때문(즉, 포함되지 않은 char랑 같은 취급)
            # 여기서 사용하지 않는 문자들은 .get method의 default값 사용
            for i in range(M - 1):
                PI[T[i]] = M - (1 + i)
            return PI
        ```
        
    - 탐색
        
        ```python
        def boyer_moore(T, P):
            PI = pre_process(P)
        
            M = len(P)
        
            # text 순회에 대한 index
            i = 0
        
            while i <= len(T) - M:
                # skip 잘 되고있나 확인
                # print(i)
        
                #
                # M번째 인덱스
                j = M - 1
                # 비교를 시작할 위치 (현재위치 + M번째 인덱스)
                k = (i) + (M - 1)
        
                # 비교할 j가 남아있고, text와 pattern이 같으면 1씩 줄여 비교
                while j >= 0 and P[j] == T[k]:
                    j -= 1
                    k -= 1
        
                # 거꾸로 비교해 가기 때문에, j가 -1이면 모두 비교가 일치했다는 뜻
                if j == -1:
                    pos = i
                    return pos
        
                # i를 비교를 시작할 위치 (초반의 k)에 해당하는 문자( T[i + M - 1] )
                # 해당 문자의 skip 테이블의 크기( PI[T[i + M - 1]] )만큼 스킵
        
                i += PI.get(T[i + M - 1], M)
        
            # 실패할 경우 -1 반환
            return -1
        
        boyer_moore(T, P)
        ```
        

(아 이런게 있구나~~)

(B형)

## 카프-라빈 알고리즘

(아 이런게 있구나~~)
