import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
s_node = int(input())
INF = int(1e9) # 모든 간선의 가중치는 10이하의 자연수이다.

# 시작노드에서 각 노드에 대해 최소 거리를 저장할 리스트
distance = [INF for _ in range(V+1)] # 최단 거리를 구하는 거니까 다 큰 값으로 설정

# 노드는 1번부터 V까지 방문 여부 확인
# visited = [False for _ in range(V+1)]

g = [[] for _ in range(V+1)] # idx 노드에 대해 [연결노드, 가중치]
for _ in range(E) :
    u, v, w = map(int, input().split())
    # g[u] = [v,w] # 하나만 연결된게 아닐수도 있으니 append
    g[u].append([v,w])

hq = []
# heapq.heappush(hq, (s_node, 0)) # (거리, 노드) 순으로 넣어야 최소 거리 순으로 pop 된다!!
heapq.heappush(hq, (0, s_node)) # (거리, 노드) 순으로 넣어야 최소 거리 순으로 pop 된다!!
# visited[s_node] = True
distance[s_node] = 0 # 시작노드에서 시작 노드까지의 (최소)거리는 0

while hq :
    # 현재 노드, 거리
    dis, now_node = heapq.heappop(hq) # 최단거리를 알아서 먼저 pop

    # 현재 노드에 대해 연결된 노드들의 최단 거리 업데이트
    # g[now_node] 개수 -> 길이만큼 검사 : 연결된 노드에 대해서 최단거리 업데이트
    # 현재 노드와 연결된 노드들의 거리가 이전 보다 짧으면 update
    # 그 중 아직 방문하지 않은 노드는 heap_push

    for i in range(len(g[now_node])) :
        # 현재 노드에 가중치를 더한것 : 현재 노드에서 연결된 노드로 넘어가는 비용이 더 적으면 update
        # 연결된 노드의 값을 update 할지 말지 결정해야 하기 때문에
        # dis[next_node]
        next_node = g[now_node][i][0]
        if g[now_node][i][1]+dis < distance[next_node] :
            distance[next_node] = g[now_node][i][1] + dis

            # if not visited[next_node] :
                # heapq.heappush(hq, (g[now_node][i][0], distance[next_node]))
            heapq.heappush(hq, (distance[next_node], g[now_node][i][0]))
                # visited[next_node] = True

for i in range(1, V+1) :
    if distance[i] == INF :
        print('INF')
        continue
    print(distance[i])

'''
다익스트라 알고리즘

1. 시작 노드에서 각 노드들까지의 거리 확인
2. 그 중 최소 노드 확인
3. 최소 노드 방문
4. 해당 노드에서 다른 노드로 이동할 때 최소 거리 갱신
5. 노드 이동시 방문 처리
'''