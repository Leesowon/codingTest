import sys
input = sys.stdin.readline
from collections import deque

def bfs() :
    d = deque()
    d.append((home_x, home_y))
    v = [False for _ in range(n)] # 편의점 방문 확인

    while d :
        x, y = d.popleft()

        if (abs(x - fest_x) + abs(y - fest_y)) <= 1000:
            print('happy')
            return

        for i in range(n) :
            nx, ny = store[i]

            if not v[i] :
                # if (abs(x-fest_x) + abs(y-fest_y)) <= 1000 :
                #     print('happy')
                #     return

                if (abs(x-nx) + abs(y-ny)) <= 1000 :
                    d.append((nx, ny))
                    v[i] = True

    print('sad')
    return

tc = int(input())
for _ in range(tc) :
    n = int(input()) # 편의점 수

    home_x, home_y = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    fest_x, fest_y = map(int, input().split())

    bfs()