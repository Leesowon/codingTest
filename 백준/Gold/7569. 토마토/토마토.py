import sys
input = sys.stdin.readline
from collections import deque

M,N,H = map(int, input().split()) # m:가로, n:세로, h:높이

dh = [-1, 1, 0, 0, 0, 0]
dn = [0, 0, -1, 1, 0, 0]
dm = [0, 0, 0, 0, -1, 1]

box = []
d = deque()

for h in range(H) :
    layer = []
    for n in range(N) :
        tomato = list(map(int, input().split()))
        layer.append(tomato)

        for m, val in enumerate(tomato) :
            if val == 1 : # 익은 토마토면
                d.append((h, n, m, 0)) # 높이, 가로, 세로, day
    box.append(layer)

ans = 0

# 우선 다 덱에 넣고, 주변 토마토를 한 번에 익게 해야한다.
while d :
    h, r, c, day = d.popleft()
    ans = max(ans, day)

    for k in range(6) :
        nh, nr, nc = h + dh[k], r + dn[k], c + dm[k]

        if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
            if box[nh][nr][nc] == 0 :
                box[nh][nr][nc] = 1
                d.append((nh, nr, nc, day+1))

for h in range(H) :
    for n in range(N) :
        if 0 in box[h][n] :
            print(-1)
            sys.exit(0)

print(ans)