import sys
input = sys.stdin.readline
from collections import deque

height, now, arrival, up, down = map(int, input().split())
building = [i for i in range(height+1)]
v = [False for _ in range(height+1)] # 1 ~ height 층

def dfs() :
    d = deque()
    d.append((now, 0))
    v[now] = True

    while d :
        current, cnt = d.popleft()
        # print(current)

        if current == arrival :
            print(cnt)
            return

        for move in (current+up, current-down) :
            if 1 <= move <= height and not v[move] : # 아직 방문 x, 갈 수 있는 층이면
                d.append((move, cnt+1))
                v[move] = True

    print('use the stairs')
    return

dfs()