import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
# 정점의 개수만큼 행렬 생성
g = [[0] * (n+1) for _ in range(n+1)]
# 정점 간의 연결을 행렬에 표시
for i in range(m) :
    a,b = map(int, input().split())
    g[a][b] = g[b][a] = 1

# 방문 여부 확인
v1 = [0] * (n+1)
v2 = v1.copy()

# 깊이 우선 탐색
def dfs(v) : # 깊이 우선 탐색
    v1[v] = 1 # 방문 처리
    print(v, end = ' ')

    for i in range(1, n+1) :
        if g[v][i] == 1 and v1[i] == 0 : # 아직 방문 x, 그래프 상 연결
            dfs(i) # 재귀 탐색

# 넓이 우선 탐색
def bfs(v) :
    q = deque()
    q.append(v)
    v2[v] = 1

    while q :
        v = q.popleft()
        print(v, end = ' ')

        for j in range(1, n+1) :
            if v2[j] == 0 and g[v][j] == 1:
                q.append(j)
                v2[j] = 1

dfs(v)
print()
bfs(v)