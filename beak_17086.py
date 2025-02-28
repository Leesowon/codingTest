import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

shark = deque()

dh = [-1, 1, 0, 0, -1, -1, 1, 1]
dw = [0, 0, -1, 1, -1, 1, -1, 1]

# 1. 상어 찾기
for i in range(n) :
    for j in range(m) :
        if g[i][j] == 1:
            shark.append((i, j))

def bfs() :
    while shark :
        h, w = shark.popleft()

        for k in range(8) :
            nh = h + dh[k]
            nw = w + dw[k]

            if nh < 0 or nh >= n or nw < 0 or nw >= m :
                continue
            if g[nh][nw] == 0:
                shark.append((nh, nw))
                g[nh][nw] = g[h][w]+1

bfs()
ans = 0

for i in range(n) :
    for j in range(m) :
        ans = max(ans, g[i][j])
print(ans-1)