# DFS (Depth Frist Search) 깊이 우선 탐색

비선형적인 그래프 구조.. 그래프로 모든 자료를 빠짐없이 검색하는것이 중요함 

(**깊이우선탐색(dfs)** / **너비우선탐색(bfs)**)

---

: 시작~ 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색하다가 더 이상 갈 곳이 없으면, 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서  다시 깊이 우선 탐색을 반복 >> 후입선출(LIFO) 구조의 스택사용

: 갈림길을 스택 or 재귀구조로 저장

>> 개념 정확히 기억

```
# 초기화
visited = []
stack = []

# 갈 곳(w)에 갔으면 W에 v를 표시해서 갔다고 표시
# 이동할 때 현 위치를 stack에 push
# 인접한 경로(간선, 엣지)는 쌍으로 제시 / 총 노드 개수도 제시
```

```
"""
1
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
1 2 /1 3/ 2 4 /2 5 /4 6 /5 6 /6 7 /3 7
# 2차원 리스트로 인접한 노드의 경로를 저장
"""
# adjl[1] : 1에 인접한 정점
def DFS(s, V) :             # s : 시작 정점 / V : 정점갯수(1번부터 시작인 정점의 마지막 정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작정점 방문 표시
    v = s                   # v : 현재정점

    while True:
        for w in adjl[v]:   # v에 인접하고, 방문 안한 w가 있으면
            if visited[w] == 0:  # 방문을 안한 곳(0)이라면
                stack.append(v) # push(v) : 현재 정점을 push
                v = w       # w에 방문
                print(v)
                visited[w] = 1 # 1로 방문 표시
                break       # v부터 다시 탐색 (갈림길)
        # 남아있는 갈림길이 없으면
        else:               # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack: # 이전 갈림길을 스택에서 꺼내서.. / if TOP > -1
                v = stack.pop() # 스택에서 꺼내기
            else: # 되돌아 갈 곳이 없으면, 남은 갈림길이 없으면 탐색종료
                break # While True의 break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # adjl :
    adjl = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E): # E개의 쌍을 2개씩 읽기
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)

    #print(adjl)
    # [[], [2, 3], [4, 5], [7], [6], [6], [7], []] .. adjl[v1].append(v2)만 있는 경우
    # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

    DFS(1,V)

```

---

## 그래프 to 코드 >> 1. 인접 행렬.ver

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/21630d15-3992-4105-a8f9-4dcfd0b07be2/%EC%BA%A1%EC%B2%98.png)

<aside>
💡

### 인접 행렬 (Adjacency Matrix)

- **인접 행렬**은 그래프의 정점들을 2차원 배열로 표현합니다. 배열의 값은 간선의 존재 여부를 나타냅니다.
- 정점의 개수가 많아지면, 메모리 사용량이 많아질 수 있습니다.
</aside>

#### 인접행렬 DFS
```
def dfs_matrix(graph, visited, v):
    # 현재 정점을 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 정점과 연결된 다른 정점을 재귀적으로 방문
    for i in range(len(graph)):
        if graph[v][i] == 1 and not visited[i]:
            dfs_matrix(graph, visited, i)

# 예제 그래프 (인접 행렬)
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# 방문 기록을 위한 리스트
visited = [False] * len(graph)

# DFS 호출
dfs_matrix(graph, visited, 0)  # 시작 정점: 0
```

#### 인접행렬 BFS
```
from collections import deque

def bfs_matrix(graph, start):
    visited = [False] * len(graph)  # 방문 기록
    queue = deque([start])  # BFS를 위한 큐
    visited[start] = True  # 시작 정점 방문 처리
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        # 현재 정점과 연결된 다른 정점을 큐에 삽입
        for i in range(len(graph)):
            if graph[v][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

# 예제 그래프 (인접 행렬)
graph = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

# BFS 호출
bfs_matrix(graph, 0)  # 시작 정점: 0
```

## 그래프 to 코드 >> 2. 인접 리스트.ver

<aside>
💡

### 인접 리스트 (Adjacency List)

- **인접 리스트**는 각 정점에 연결된 다른 정점들을 리스트로 표현합니다.
- 메모리 사용량이 적고, 특정 정점과 연결된 정점들을 빠르게 탐색할 수 있습니다.
</aside>

#### 인접리스트 DFS
```
def dfs_list(graph, visited, v):
    # 현재 정점을 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    # 현재 정점과 연결된 다른 정점을 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_list(graph, visited, i)

# 예제 그래프 (인접 리스트)
graph = [
    [1, 2],    # 정점 0과 연결된 정점들
    [0, 2, 3], # 정점 1과 연결된 정점들
    [0, 1, 3], # 정점 2와 연결된 정점들
    [1, 2]     # 정점 3과 연결된 정점들
]

# 방문 기록을 위한 리스트
visited = [False] * len(graph)

# DFS 호출
dfs_list(graph, visited, 0)  # 시작 정점: 0
```

#### 인접리스트 BFS
```
from collections import deque

def bfs_list(graph, start):
    visited = [False] * len(graph)  # 방문 기록
    queue = deque([start])  # BFS를 위한 큐
    visited[start] = True  # 시작 정점 방문 처리
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        # 현재 정점과 연결된 다른 정점을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 예제 그래프 (인접 리스트)
graph = [
    [1, 2],    # 정점 0과 연결된 정점들
    [0, 2, 3], # 정점 1과 연결된 정점들
    [0, 1, 3], # 정점 2와 연결된 정점들
    [1, 2]     # 정점 3과 연결된 정점들
]

# BFS 호출
bfs_list(graph, 0)  # 시작 정점: 0
```
