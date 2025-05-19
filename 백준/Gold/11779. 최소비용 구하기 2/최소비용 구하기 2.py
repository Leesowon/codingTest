import sys, heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]
for _ in range(m) :
    start, end, weight = map(int, input().split())
    bus[start].append([weight, end])

a, b = map(int, input().split())

h = []
heapq.heappush(h, (0, a)) # 시작위치에서 시작위치로 가는 비용은 0

route = [1e9 for _ in range(n+1)] # 각 도시에 대해 갈 수 있는 비용 (최댓값으로 초기화)
route[a] = 0

prev_node = [0 for _ in range(n+1)]

while h :
    dist, now_node = heapq.heappop(h) # 현재 위치까지의 비용, 현재 위치

    if now_node == b :
        break

    for i in range(len(bus[now_node])) :
        next_node = bus[now_node][i][1]
        weight = bus[now_node][i][0]

        if route[now_node] + weight < route[next_node] :
            route[next_node] = route[now_node] + weight
            heapq.heappush(h, (dist+weight, next_node))
            prev_node[next_node] = now_node

path = [b]
now = b

while now != a :
    now = prev_node[now]
    path.append(now)

print(route[b])
path.reverse()
print(len(path))
print(' '.join(map(str, path)))