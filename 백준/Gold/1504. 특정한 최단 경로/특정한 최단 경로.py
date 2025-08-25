import sys, heapq
input = sys.stdin.readline

# 이동했던 간선도 다시 이동할 수 있다.
# but 반드시 최단 경로로 이동해야한다.
# 1 -> N 사이에 두 정정을 반드시 거쳐야 한다.

INF = 10**15

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w)) # 목적지, 가중치
    graph[v].append((u, w)) # 양방향 존재

v1, v2 = map(int, input().split())

def dijkstra(start) :
    distance = [INF] * (N + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, node = heapq.heappop(q)

        if distance[node] < dist :
            continue

        # 현재 노드와 연결된 노드 중 최단 탐색
        for i in graph[node] : # i : (u, v)
            next_node = i[0]
            next_weight = i[1]

            if distance[node] + next_weight < distance[next_node] :
                distance[next_node] = distance[node] + next_weight
                heapq.heappush(q, (distance[node] + next_weight, next_node))
    return distance

# 시작은 1, 도착 N
d1 = dijkstra(1)
dv1 = dijkstra(v1)
dv2 = dijkstra(v2)

route1 = d1[v1] + dv1[v2] + dv2[N] # 1 -> v1 -> v2
route2 = d1[v2] + dv2[v1] + dv1[N] # 1 -> v2 -> v1
ans = min(route1, route2)

print(ans if ans < INF else -1)
