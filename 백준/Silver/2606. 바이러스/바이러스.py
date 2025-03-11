import sys
input = sys.stdin.readline
from collections import deque

v = int(input()) # 컴퓨터 수
e = int(input()) # 네트워크 연결된 쌍의 수
com = [[0] * (v+1) for _ in range(v+1)] # 컴퓨터가 1부터 시작)

for _ in range(e) :
    a,b = map(int, input().split())
    com[a][b] = com[b][a] = 1

v_dfs = [0] * (v+1)
v_bfs = [0] * (v+1)

cnt_dfs = 0
cnt_bfs = 0

# 깊이 우선 탐색 -> 큐
def dfs(n) :
    global cnt_dfs

    v_dfs[n] = 1
    cnt_dfs += 1

    for i in range(1, v+1) : # 컴퓨터 1~(n+1)
        if v_dfs[i] == 0 and com[n][i] == 1 :
            dfs(i)

def bfs(n) :
    global cnt_bfs
    d = deque()

    d.append(n)
    v_bfs[n] = 1

    while d :
        cur_n = d.popleft()

        for i in range(1, v+1) :
            if v_bfs[i] == 0 and com[i][cur_n] == 1 :
                d.append(i)
                cnt_bfs += 1
                v_bfs[i] = 1

dfs(1)
print(cnt_dfs-1) # 첫번째 컴 빼기