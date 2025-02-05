import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
q = deque()
visited = [[False] * m for _ in range(n)] # 거리를 또 계산하지 않기 위해
ans = [[0]*m for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 시작점 찾기
for r in range(n) :
    for c in range(m) :
        if g[r][c] == 2 :
            visited[r][c] = True
            q.append((r,c))

while q :
    h, w = q.popleft()

    for i in range(4) :
        nh = h + dh[i]
        nw = w + dw[i]

        if nh < 0 or nh >= n or nw < 0 or nw >= m:
            continue
        if g[nh][nw] != 1 :  # 방문할 수 없는 거리
            continue
        if visited[nh][nw]:  # 방문했던 곳이면 continue
            continue

        q.append((nh, nw))
        visited[nh][nw] = True
        ans[nh][nw] = ans[h][w] + 1 # 이전 거리 +1 ****

for i in range(n) :
    for j in range(m) :
        if not visited[i][j] and g[i][j] == 1 : # ****
            print(-1, end=" ")
        else :
            print(ans[i][j], end = ' ')
    print()