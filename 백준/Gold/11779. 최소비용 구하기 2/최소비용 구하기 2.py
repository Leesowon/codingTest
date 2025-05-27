import sys, heapq
input = sys.stdin.readline

n = int(input()) # 도시
m = int(input()) # 버스
bus = [[] for _ in range(n+1)]

for _ in range(m) :
    start, end, weight = map(int, input().split())
    bus[start].append([weight, end])
s, e = map(int, input().split())

# 출발 지점으로부터 도착했을 때의 최소 경로 저장
distance = [1e9 for _ in range(n+1)]
distance[s] = 0

pre_node = [0 for _ in range(n+1)]
h = []
# 시작 위치에서 출발 : 출발 위치에 대한 비용은 0
heapq.heappush(h, (0, s))

while h:
    w, node = heapq.heappop(h) # 현재 위치

    if node == e :
        break

    # 현재 위치에서 갈 수 있는 다음 위치들에 대해 업데이트 가능한지 -
    for i in range(len(bus[node])) :
        next_node = bus[node][i][1] # 다음 위치
        new_weight = w + bus[node][i][0] # 현재 위치에서 다음 위치로 이동하는 비용

        # 현재 위치에서 이동할 수 있는 거리 중 값이 더 작다면 갱신
        if new_weight < distance[next_node] :
            distance[next_node] = new_weight
            heapq.heappush(h, (new_weight, next_node))
            pre_node[next_node] = node

# 거꾸로 확인하면서 이동 경로 찾기
path = [e]
now = e

while now != s :
    now = pre_node[now]
    path.append(now)

path.reverse()

print(distance[e])
print(len(path))
print(" ".join(map(str, path)))
