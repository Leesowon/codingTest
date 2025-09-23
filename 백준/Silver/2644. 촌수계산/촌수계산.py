import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 사람 수
s,e = map(int, input().split())
m = int(input()) # 관계
relation = []
for _ in range(m) :
    relation.append(list(map(int, input().split())))

# dfs
v = [False] * (m+1) # 관계 수만큼
q = deque()

INF = 10**9
ans = INF

for i in range(m) :
    for j in range(2) :
        if relation[i][j] == s:
            q.append((i, abs(j-1), 1)) # 부모 관계
            v[i] = True

            while q :
                cur_i, cur_j, rel = q.popleft()

                if relation[cur_i][cur_j] == e :
                    ans = min(ans, rel)
                    break

                for k in range(m) :
                    for l in range(2):
                        if relation[k][l] == relation[cur_i][cur_j] and not v[k] :
                            q.append((k, abs(l - 1), rel+1))
                            v[k] = True

if ans == INF :
    print(-1)
else :
    print(ans)