import sys
input = sys.stdin.readline
from collections import deque

# 탈출하는 가장 빠른 길 -> bfs
INF = float('inf')
while True :
    L, R, C = map(int, input().split()) # 층수, 행, 열

    if L == 0 and R == 0 and C == 0 :
        sys.exit(0)

    # # : 지나갈 수 없는 칸
    # . : 빈 칸 -> 지나갈 수 있는 칸
    # E : 탈출구

    dl = [-1, 1, 0, 0, 0, 0]
    dr = [0, 0, -1, 1, 0, 0]
    dc = [0, 0, 0, 0, -1, 1]

    d = deque()
    v = [[[False] * C for _ in range(R)] for _ in range(L)]

    building = []
    for l in range(L) :
        floor = []
        for r in range(R) :
            floor.append(input())

            for c in range(C) :
                if floor[r][c] == 'S' :
                    d.append((l, r, c, 0))
                    v[l][r][c] = True

        building.append(floor)
        input()

    ans = INF
    while d :
        l, r, c, x = d.popleft()

        for k in range(6) :
            nl = l + dl[k]
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C :
                if not v[nl][nr][nc] :
                    if building[nl][nr][nc] == 'E' :
                        ans = min(ans, x+1) # 이동했음을 고려
                    if building[nl][nr][nc] == '.' :
                        v[nl][nr][nc] = True
                        d.append((nl, nr, nc, x+1))

    if ans == INF :
        print("Trapped!")
    else :
        print(f"Escaped in {ans} minute(s).")