import sys
input = sys.stdin.readline
from collections import deque

tc = int(input())

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

for _ in range(tc) :
    M, N, K = map(int, input().split()) # 가로, 세로, 배추 위치

    v = [[False] * M for _ in range(N)]
    g = [[0] * M for _ in range(N)]

    for _ in range(K) :
        c, r = map(int, input().split())
        g[r][c] = 1

    cnt = 0
    d = deque()
    for i in range(N) :
        for j in range(M) :
            if g[i][j] == 1 and not v[i][j] :
                v[i][j] = True
                d.append((i, j))
                cnt += 1

                while d :
                    cur_r, cur_c = d.popleft()

                    for k in range(4) :
                        nr = cur_r + dh[k]
                        nc = cur_c + dw[k]

                        if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] :
                            if g[nr][nc] == 1 :
                                d.append((nr, nc))
                                v[nr][nc] = True

    print(cnt)