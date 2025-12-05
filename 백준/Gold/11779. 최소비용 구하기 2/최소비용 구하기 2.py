import sys
input = sys.stdin.readline
import heapq as hq

n = int(input()) # 도시의 수 (노드)
m = int(input()) # 버스의 수

h = []
g = [[] for _ in range(n+1)]

pre = [0 for _ in range(n+1)]

INF = 1e9
distance = [INF] * (n+1)

for _ in range(m) :
    u, v, w = map(int, input().split()) # 출발, 도착, 비용
    g[u].append([v, w]) # 도착, 비용

start, end = map(int, input().split())
distance[start] = 0
hq.heappush(h, (0, start))

while h :
    weight, cur = hq.heappop(h)

    if cur == end :
        break

    for next_start, next_cost in g[cur] :

        if distance[next_start] > distance[cur] + next_cost :
            distance[next_start] = distance[cur] + next_cost

            pre[next_start] = cur

            hq.heappush(h, (distance[cur] + next_cost, next_start))

path = [end]
p = end

while True :
    if p == start :
        break

    path.append(pre[p])
    p = pre[p]

path.reverse()

print(distance[end]) # 최소 비용
print(len(path))
print(' '.join(map(str, path)))