import sys, heapq
input = sys.stdin.readline
'''
N명의 학생이 X번 마을에 모여서 파티를 벌이기로 하였다.
M개의 단방향 도로, Ti 시간 소요
최단시간으로 갔다가 돌아오려고 한다.
가장 많은 시간이 걸리는 학생은?

왜 다익스트라를 선택하였는가 -> 방향이 있는 거리의 최단 거리를 구하는 문제
'''

INF = 1e9

N, M, X = map(int, input().split())
# M개의 도로에 대한 (시작 마을, 도착 마을, 소요시간/비용)
dp_ori = [[] for _ in range(N+1)] # 1~N번 마을 연결 정보
dp_rev = [[] for _ in range(N+1)]

for _ in range(M) :
    start, end, cost = map(int, input().split())
    dp_ori[start].append([end, cost])
    dp_rev[end].append([start, cost])

def dijkstra(start_node, dp) :
    '''
    다익스트라란?
        시작점에 대해 모든 노드에 대한 최단 거리 return
        시작점과 연결된 값 확인
        그 중 최단 거리 갱신
    '''

    dist = [INF for _ in range(N + 1)]  # 최단거리를 저장하는 list
    # dist_rev = [INF for _ in range(N+1)]

    hq = []
    heapq.heappush(hq, (0, start_node)) # (거리, 시작노드) : 시작 노드에 대한 거리는 0

    dist[start_node] = 0
    # dist_rev[start_node] = 0

    while hq : # 모든 경로에 대해 확인 - 갱신 or not
        now_dist, node = heapq.heappop(hq)

        # 현재 노드와 연결된 도로의 수만큼 반복
        for i in range(len(dp[node])) :
            # 현재 노드와 연결된 노드까지의 경로에 대해 만약 현재 노드에서 이동하는게 더 적은 비용이 든다면 갱신
            next_node = dp[node][i][0]
            distance = dp[node][i][1]
            if dist[node] + distance < dist[next_node] :
                dist[next_node] = dist[node] + distance
                heapq.heappush(hq, (dist[next_node], next_node))
            #
            # if dist_rev[node] + distance < dist_rev[next_node] :
            #     dist_rev[next_node] = dist_rev[node] + distance
    return dist

from_x = dijkstra(X, dp_ori) # X 마을에서 각 마을로 돌아가는 최단 거리
to_x = dijkstra(X, dp_rev) # 각 마을에서 X로 가는 최단거리

max_dist = -INF
for i in range(1, N+1) : # 1번 마을부터 N번 마을까지
    if from_x[i] == INF or to_x[i] == INF :
        continue
    sum_dist = from_x[i] + to_x[i]
    max_dist = max(max_dist, sum_dist)

print(max_dist)