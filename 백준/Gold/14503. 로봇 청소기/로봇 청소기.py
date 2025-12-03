import sys
input = sys.stdin.readline

N, M = map(int, input().split())
R, C, D = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

dh = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]

def in_range(r, c) :
    return 0 <= r < N and 0 <= c < M

def cleaner(r, c, d) :
    cnt = 0

    while True :
        # 1번 청소하고 청소 횟수 1회 증가
        if g[r][c] == 0 :
            g[r][c] = -1 # 청소함
            cnt += 1

        for _ in range(4) :
            d = (d-1) % 4

            nr = r + dh[d]
            nc = c + dw[d]

            if in_range(nr, nc) and g[nr][nc] == 0 :
                r, c = nr, nc
                break # 이동했으면 다시 1번으로

        else:
            # 후진
            r = r + dh[d] * (-1)
            c = c + dw[d] * (-1)

            if in_range(r, c) and g[r][c] == 1 or not in_range(r, c) : # 벽이라면
                print(cnt)
                return

cleaner(R, C, D)