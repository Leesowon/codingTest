import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n+1)] # 각 도시로 이동하는데에 대한 비용

for _ in range(m) :
    u, v, w = map(int, input().split())
    bus[u].append([v,w])
start, end = map(int, input().split())

hq = []
heapq.heappush(hq, (0, start))
distance = [1e9 for _ in range(n+1)]
distance[start] = 0 # 시작 위치에 대해

while hq :
    dist, now = heapq.heappop(hq)

    # 현재 위치에 대해 bus[now] = [도착, 비용]

    if now == end :
        break

    # 현재 위치에서 이동할 수 있다면 heappush
    for i in range(len(bus[now])) :
        next_location = bus[now][i][0]
        new_dist = dist + bus[now][i][1]

        if new_dist < distance[next_location] :
            distance[next_location] = new_dist
            heapq.heappush(hq, (new_dist, next_location))

print(distance[end])