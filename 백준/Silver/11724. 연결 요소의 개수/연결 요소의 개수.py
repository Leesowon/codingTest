import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split()) # 정점, 간선

g = [[] for _ in range(n+1)] # 정점은 1부터
visit = [False] * (n+1)

for _ in range(m) : # O(m)
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

def dfs(node) :
    visit[node] = True

    for nxt_node in g[node] :
        if not visit[nxt_node] :
            dfs(nxt_node)

ans = 0
for i in range(1, n+1) :
    if not visit[i] :
        dfs(i)
        ans += 1

print(ans)