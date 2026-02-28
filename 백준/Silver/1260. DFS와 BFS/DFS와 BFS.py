import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())

g = [[0] * (n+1) for _ in range(n + 1)]  # 노드는 1~n번까지

# 정점 간의 연결 표시
for _ in range(m):
    n1, n2 = map(int, input().split())
    g[n1][n2] = g[n2][n1] = 1

v_bfs = [0] * (n+1)
v_dfs = v_bfs.copy()

def dfs(v) :
    v_bfs[v] = 1
    print(v, end=' ')

    for i in range(1, n+1) :
        if g[v][i] == 1 and v_bfs[i] == 0 :
            dfs(i)

def bfs(v) :
    d = deque()

    d.append(v)
    v_dfs[v] = 1

    while d :
        node = d.popleft()
        print(node, end=' ')

        for j in range(1, n+1) :
            if v_dfs[j] == 0 and g[node][j] == 1 :
                d.append(j)
                v_dfs[j] = 1

dfs(v)
print()
bfs(v)