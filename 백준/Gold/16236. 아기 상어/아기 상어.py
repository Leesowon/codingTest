import sys, copy
from collections import deque
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def find_fish() :
    global s_size, g
    eatable = []
    for i in range(N) :
        for j in range(N) :
            if g[i][j] in fish and g[i][j] < s_size :
                eatable.append([i,j])
    return eatable

def bfs(sh, sw):
    global g, s_size
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((sh, sw))
    visited[sh][sw] = 0
    fishes = []

    while q:
        h, w = q.popleft()
        for k in range(4):
            nh = h + dh[k]
            nw = w + dw[k]

            if 0 <= nh < N and 0 <= nw < N and visited[nh][nw] == -1:
                # 지나갈 수 있는 길
                if g[nh][nw] <= s_size:
                    visited[nh][nw] = visited[h][w] + 1
                    q.append((nh, nw))
                    # 먹을 수 있는 물고기
                    if 0 < g[nh][nw] < s_size:
                        fishes.append((visited[nh][nw], nh, nw))

    fishes.sort()  # 거리 → 행 → 열
    return fishes


N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]
s_size = 2
size_cnt = 0
time = 0
fish = [1,2,3,4,5,6]

while True:
    sh, sw = -1, -1
    for i in range(N):
        for j in range(N):
            if g[i][j] == 9:
                sh, sw = i, j

    fishes = bfs(sh, sw)
    if not fishes:
        break

    dist, fx, fy = fishes[0]
    time += dist
    size_cnt += 1
    if size_cnt == s_size:
        s_size += 1
        size_cnt = 0

    g[sh][sw] = 0
    g[fx][fy] = 9


print(time)