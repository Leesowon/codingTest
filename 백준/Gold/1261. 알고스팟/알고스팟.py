import sys, heapq
input = sys.stdin.readline
from collections import deque

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

M, N = map(int, input().split())
g = [list(input().strip()) for _ in range(N)]

INF = 1e9
# dfs 인데 최단 거리가 아니라 최소 벽 뚫는 갯수
walls = [[INF] * M for _ in range(N)] # 해당 위치를 방문했을 때 뚫어야 하는 벽의 수 (최소로 갱신)
walls[0][0] = 0

def dfs(sh, sw):
    global wall

    # d = deque()
    # d.append((sh, sw))

    hq = []
    heapq.heappush(hq, (0, sh, sw)) # 벽의 수, 좌표

    while hq :
        wall, h, w = heapq.heappop(hq)
        # print(f"h, w : {h, w}")

        for k in range(4) :
            nh = h + dh[k]
            nw = w + dw[k]

            if nh == N and nw == M :
                break

            # 범위를 벗어나거나
            if nh < 0 or nh >= N or nw <0 or nw >= M :
                continue

            if walls[nh][nw] != INF : # 이전에 체크 했다면
                continue

            # 벽이면 더 적은 수로 갱신
            if g[nh][nw] == '1' :
                # print("벽")
                # print(f"wall[h][w] : {walls[h][w]+1}, wall[nh][nw] : {walls[nh][nw]}")
                if walls[h][w] + 1 < walls[nh][nw] :
                    walls[nh][nw] = walls[h][w] + 1
                    heapq.heappush(hq, (wall+1, nh, nw))
            # 벽이 아니면 그냥 이동
            else :
                # print("벽 아님")
                if walls[h][w] < walls[nh][nw]:
                    walls[nh][nw] = walls[h][w]
                    heapq.heappush(hq, (wall, nh, nw))

            # print(f"벽 갱신 {h, w} : {walls[nh][nw]}")

dfs(0,0)
print(walls[N-1][M-1])