import sys
input = sys.stdin.readline
from collections import deque

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

INF = 10**9

tc = int(input())

for _ in range(tc) :
    w, h = map(int, input().split())

    d = deque()
    d_fire = deque()

    v = [[False] * w for _ in range(h)]
    fire_day = [[INF] * w for _ in range(h)]

    # 입력 받으면서 상근이의 위치와 day 0의 불의 위치 저장
    g = []
    for i in range(h) :
        floor = list(input().strip())
        g.append(floor)

        for j in range(w) :
            if floor[j] == '@' :
                v[i][j] = True
                d.append((i, j, 0))

            if floor[j] == '*' :
                d_fire.append((i, j, 0))
                fire_day[i][j] = 0

    while d_fire :
        r, c, day = d_fire.popleft()

        day += 1

        for k in range(4) :
            nr = r + dh[k]
            nc = c + dw[k]

            if 0 <= nr < h and 0 <= nc < w and g[nr][nc] != '#' :
                if fire_day[nr][nc] > day :
                    fire_day[nr][nc] = day
                    d_fire.append((nr, nc, day))

    ck = True
    while d and ck :
        r, c, day = d.popleft()

        day += 1

        for k in range(4) :
            nr = r + dh[k]
            nc = c + dw[k]

            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                print(day)
                ck = False
                break

            if v[nr][nc]:
                continue

            if g[nr][nc] == '#' :
                continue

            if fire_day[nr][nc] > day :
                v[nr][nc] = True
                d.append((nr, nc, day))

    if ck :
        print("IMPOSSIBLE")