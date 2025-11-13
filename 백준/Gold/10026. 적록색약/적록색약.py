import sys
sys.setrecursionlimit(10**6) # 파이썬 재귀 깊이 지정
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(input().strip()) for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

d = deque()
v = [[False] * n for _ in range(n)]

ans_normal = 0 # 적록색약이 아닌 사람
ans_medi = 0 # 적록색약인 사람

def dfs(r, c, color) :
    v[r][c] = True

    for k in range(4) :
        nr = r + dh[k]
        nc = c + dw[k]

        if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] :
            if g[nr][nc] == color :
                dfs(nr, nc, color)

for color in ['R', 'G', 'B'] :
    for i in range(n) :
        for j in range(n) :
            if not v[i][j] and g[i][j] == color :
                dfs(i, j, color)
                ans_normal += 1

# 기존 그래프에서 G -> R로 변경
for i in range(n) :
    for j in range(n) :
        if g[i][j] == 'G' :
            g[i][j] = 'R'

# 방문 정보 초기화
v = [[False] * n for _ in range(n)]

for color in ['R', 'B'] :
    for i in range(n) :
        for j in range(n) :
            if not v[i][j] and g[i][j] == color :
                dfs(i, j, color)
                ans_medi += 1

print(ans_normal, ans_medi)