import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 빙하 수
def count() :
    global n, m, dh, dw, ice

    d = deque()
    v = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n) :
        for j in range(m) :
            if ice[i][j] != 0 and not v[i][j] :
                cnt += 1
                v[i][j] = True
                d.append((i, j))

                while d :
                    r, c = d.popleft()
                    # print(f"r : {r}, c : {c}")

                    for k in range(4) :
                        nr = r + dh[k]
                        nc = c + dw[k]

                        if 0 <= nr < n and 0 <= nc < m and not v[nr][nc] :
                            if ice[nr][nc] != 0 :
                                v[nr][nc] = True
                                d.append((nr, nc))
    return cnt

# 빙하 녹이기
def melt() :
    global n, m, dh, dw, ice

    mel = [[0] * m for _ in range(n)]

    # 빙하를 발견하면, 상하좌우 확인해서 0 확인
    for i in range(n) :
        for j in range(m) :
            if ice[i][j] != 0 :

                for k in range(4) :
                    nr = i + dh[k]
                    nc = j + dw[k]

                    if 0 <= nr < n and 0 <= nc < m and ice[nr][nc] == 0 :
                        mel[i][j] += 1

    for i in range(n) :
        for j in range(m) :
            if ice[i][j] - mel[i][j] > 0 :
                ice[i][j] -= mel[i][j]
            else :
                ice[i][j] = 0

ans = 0
while True :
    if count() >= 2 :
        break
    cnt_0 = 0
    for ic in ice :
        cnt_0 += ic.count(0)

    if cnt_0 == n * m :
        print(0)
        sys.exit(0)

    melt()
    ans += 1

print(ans)