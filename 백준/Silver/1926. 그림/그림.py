import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n : 세로, m : 가로
g = []
d = deque()

for i in range(n) :
    g.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

num = 0 # 그림의 개수
max_area =0

# 1을 찾으면 bfs 시작
for i in range(n) :
    for j in range(m) :
        if g[i][j] == 1 and not visited[i][j]:
            d.append((i,j)) # 그림 시작 위치 & 크기
            visited[i][j] = True
            area = 0
            num += 1

            while d :
                h, w, = d.popleft()
                area += 1

                # 상하좌우 이동하려고 하는데
                # 해당 위치의 값이 1이고, 아직 방문하지 않았고 (체크x), 범위를 벗어나지 않으면 이동
                # 이동할 수 없는 위치면 continue
                for k in range(4):
                    nh = h + dh[k]
                    nw = w + dw[k]

                    if nh < 0 or nh >= n or nw < 0 or nw >= m :
                        continue
                    if visited[nh][nw] : # true이면 이미 방문한 곳
                        continue
                    if g[nh][nw] != 1 :
                        continue

                    # 이동할 수 있는 조건이면
                    d.append((nh, nw))
                    visited[nh][nw] = True

            # 해당 1이 시작하는 곳에서 넓이를 다 구했으면
            max_area = max(area, max_area)

print(num)
print(max_area)