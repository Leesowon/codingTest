import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

v = [False for _ in range(100001)]

def dfs() :
    d = deque()
    d.append((n, 0))
    v[n] = True

    while d :
        x, cnt = d.popleft()

        if x == k:
            return cnt

        if (0 <= x+1 <= 100000) and not v[x+1] :
            d.append((x + 1, cnt + 1))
            v[x+1] = True

        if (0 <= x-1 <= 100000) and not v[x-1] :
            d.append((x - 1, cnt + 1))
            v[x - 1] = True

        if (0 <= x*2 <= 100000) and not v[x*2] :
            d.append((x * 2, cnt + 1))
            v[x * 2] = True

print(dfs())