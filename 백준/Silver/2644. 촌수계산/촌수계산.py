import sys
input = sys.stdin.readline

n = int(input()) # 사람 수
s,e = map(int, input().split())
m = int(input()) # 관계
g = [[] for _ in range(n+1)]
visited = [False] * (n+1)

result = []

# 어떤 노드들이 연결되었는지 g배열에 2차원으로 저장
for _ in range(m) :
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

def dfs(v, num) : # v : 사람 번호, num : 촌 수
    if v == e :
        result.append(num)

    num += 1
    visited[v] = True

    for i in g[v] :
        if not visited[i] :
            dfs(i, num)

dfs(s, 0)

if len(result) == 0 :
    print(-1)
else :
    print(min(result))

