import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(input().strip()) for _ in range(n)]

v_nor = [[False] * n for _ in range(n)]
v_blind = [[False] * n for _ in range(n)]

# 이동방향 - 상하좌우
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

d_nor = deque()
d_blind = deque()
zone_nor = 0
zone_blind = 0

# 적록색약 x
for i in range(n) :
    for j in range(n) :
        if not v_nor[i][j] : # 아직 방문하지 않은 이전과 다른 색을 찾으면
            d_nor.append((i,j))
            v_nor[i][j] = True
            zone_nor += 1

        while d_nor : # 같은 색 찾기
            h, w = d_nor.popleft()
            now_color = g[h][w] # 현재 색깔

            for k in range(4) :
                nh = h + dh[k]
                nw = w + dw[k]

                if nh < 0 or nh >= n or nw < 0 or nw >= n :
                    continue
                if v_nor[nh][nw] :
                    continue
                if g[nh][nw] != now_color :
                    continue

                d_nor.append((nh, nw))
                v_nor[nh][nw] = True

# 적록 색약
for i in range(n) :
    for j in range(n) :
        if not v_blind[i][j] :
            d_blind.append((i,j))
            v_blind[i][j] = True
            zone_blind += 1  # 새로운 색을 찾으면

        while d_blind :
            h, w = d_blind.popleft()
            now_color = g[h][w]

            for k in range(4) :
                nh = h + dh[k]
                nw = w + dw[k]

                if nh < 0 or nh >= n or nw <0 or nw >= n :
                    continue
                if v_blind[nh][nw] :
                    continue

                # '현재 색이 파랑색일 때는 다른 색으로 볼 수 없다.
                if now_color == 'B' :
                    if g[nh][nw] != 'B' :
                        continue
                # 현재 색이 빨강 or 초록일 때 파랑이 아니면 된다.
                if now_color == 'R' :
                    if g[nh][nw] == 'B' :
                        continue
                if now_color == 'G' :
                    if g[nh][nw] == 'B' :
                        continue

                d_blind.append((nh, nw))
                v_blind[nh][nw] = True

print(zone_nor, zone_blind)