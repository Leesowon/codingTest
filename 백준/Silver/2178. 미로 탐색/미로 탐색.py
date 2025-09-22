import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]

v = [[False] * m for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

d = deque()
d.append((0,0,1))
v[0][0] = True

ans_distance = float('inf')

while d :
    h, w, dis = d.popleft()

    if h == (n-1) and w == (m-1) :
        ans_distance = min(ans_distance, dis)
        break

    for i in range(4) :
        nh = h + dh[i]
        nw = w + dw[i]

        if nh < 0 or nh >= n or nw < 0 or nw >= m :
            continue
        if v[nh][nw] :
            continue
        if maze[nh][nw] != '1' :
            continue

        d.append((nh, nw, dis+1))
        v[nh][nw] = True

print(ans_distance)