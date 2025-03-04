import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())

# 1. 정점의 개수만큼 행렬 생성
g = [[0] * (n+1) for _ in range(n+1)]

# 2. 정점 간의 연결을 행렬에 표시
for i in range(m) :
    a,b = map(int, input().split())
    g[a][b] = g[b][a] = 1

# 3. 방문 여부 확인
bfs_v = [0] * (n+1)
dfs_v = [0] * (n+1)

# 4-1. 너비 우선 탐색
def bfs(v) :
    d = deque()
    d.append(v)
    bfs_v[v] = 1

    while d :
        v = d.popleft()
        print(v, end=' ')

        for j in range(1, n+1) : # 1번 정점부터 n번 정점까지 확인
            if bfs_v[j] == 0 and g[j][v] == 1:
                d.append(j)
                bfs_v[j] = 1

# 4-2. 깊이 우선 탐색
def dfs(v) :
    dfs_v[v] = 1
    print(v, end=' ')

    for k in range(1, n+1) :
        if dfs_v[k] == 0 and g[k][v] == 1:
            dfs(k)

dfs(v)
print()
bfs(v)
