import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
d = deque(arr)
ans = []

while d :
    for _ in range(k-1) :
        tmp = d.popleft()
        d.append(tmp)
    ans.append(d.popleft())

print(f"<{', '.join(map(str, ans))}>")