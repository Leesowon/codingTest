import sys
input = sys.stdin.readline
from collections import deque

dh = [-1, -2, -2, -1, 1, 2, 2, 1]
dw = [-2, -1, 1, 2, -2, -1, 1, 2]

tc = int(input())

for _ in range(tc) :
    d = deque()

    l = int(input()) # 한 변의 길이 (l x l)
    cur_r, cur_c = map(int, input().split())
    dis_r, dis_c = map(int, input().split())
    v = [[False] * l for _ in range(l)]

    d.append((cur_r, cur_c, 0))
    v[cur_r][cur_c] = True

    # ans = 1e9
    while d :
        r, c, move = d.popleft()

        if r == dis_r and c == dis_c:
            print(move)
            break

        move += 1
        for k in range(8) :
            nr = r + dh[k]
            nc = c + dw[k]

            if 0 <= nr < l and 0 <= nc < l :
                if not v[nr][nc] :

                    d.append((nr, nc, move))
                    v[nr][nc] = True
    # print(ans)