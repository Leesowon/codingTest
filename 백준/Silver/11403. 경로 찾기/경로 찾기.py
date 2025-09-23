import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for _ in range(n)]

def dfs(start, cur, v) :
    for nxt in range(n) :
        if g[cur][nxt] == 1 :
            ans[start][nxt] = 1
            if not v[nxt] : # 방문 여부는 도달 여부와 별개로 처리해줘야 함
                v[nxt] = True
                dfs(start, nxt, v)

# 어디에 도착하는게 중요하지 않음
# 그냥 스쳐?지나가면 1
for i in range(n) :
    visited = [False] * n
    dfs(i, i, visited) # 시작, 현재, 끝

for row in ans :
    print(*row)