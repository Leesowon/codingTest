import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
adj = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문 처리

dp= [[0,1] for _ in range(n+1)]

def dfs(v) :
    visited[v] = True

    for next in adj[v] : # 인접한 노드 방문
        if (visited[next]) : # 방문했다면 넘어가기
            continue
        dfs(next) # 인접한 다음 노드에 대해 dfs
        dp[v][0] += dp[next][1] # 내가 얼리어답터가 아니면 자식노드가 얼리어답터이어야 한다.
        dp[v][1] += min(dp[next]) # 내가 얼리어답터면 자식노드가 무엇인지 상관 x

for i in range(n-1) :
    f, t = map(int, input().split())
    adj[f].append(t)
    adj[t].append(f)

dfs(1) # 아무노드에서 시작해도 상관 x
print(min(dp[1]))