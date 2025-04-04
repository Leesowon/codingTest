import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split()) # 세로, 가로, 직사각형 갯수
g = [[0] * N for _ in range(M)]

for _ in range(K) :
    x1, y1, x2, y2 = map(int, input().split())
    for r in range(x1, x2) :
        for c in range(y1, y2) :
            g[c][r] = 1

v = [[False] * N for _ in range(M)]
d = deque()

area_li = []

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

for i in range(M) :
    for j in range(N) :
        if g[i][j] == 0 and not v[i][j] :
            area = 1
            d.append((i, j))
            v[i][j] = True

            while d :
                h, w = d.popleft()

                for k in range(4) :
                    nh = h + dh[k]
                    nw = w + dw[k]

                    if nh < 0 or nh >= M or nw < 0 or nw >= N :
                        continue
                    if v[nh][nw] :
                        continue
                    if g[nh][nw] != 0 :
                        continue

                    area += 1
                    d.append((nh, nw))
                    v[nh][nw] = True

            area_li.append(area)

print(len(area_li))
area_li.sort()
print(' '.join(map(str, area_li)))