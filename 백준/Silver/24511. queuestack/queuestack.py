import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split())) # stack(1) or queue(0)
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

d = deque()
ans = []

# 큐의 영향을 받는 값만 덱에 넣기
for i in range(N) :
    if A[i] == 0 :
        d.append(B[i])

for num in C :
    d.appendleft(num) # 맨 앞에 넣기
    print(d.pop(), end=' ')
