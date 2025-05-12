import sys, heapq
input = sys.stdin.readline

n = int(input())
max_heap = [] # 양수만 들어가는 최대 힙
min_heap = [] # 음수만 들어가는 최소 힙

for _ in range(n) :
    num = int(input())
    if num > 0 :
        heapq.heappush(max_heap, -num)
    else :
        heapq.heappush(min_heap, num)

ans = 0

while max_heap :
    if len(max_heap) < 2 :
        ans += -heapq.heappop(max_heap)
        break

    n1 = -heapq.heappop(max_heap)
    n2 = -heapq.heappop(max_heap)

    if n1 == 1 or n2 == 1 :
        ans += (n1+n2)
        continue

    ans += n1 * n2

while min_heap :
    if len(min_heap) < 2:
        ans += heapq.heappop(min_heap)
        break

    n1 = heapq.heappop(min_heap)
    n2 = heapq.heappop(min_heap)

    ans += n1 * n2

print(ans)