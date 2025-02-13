import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
h = list(map(int, input().split()))
heapq.heapify(h)

# 항상 힙의 길이는 k로 유지
ans = []
for _ in range(k) :
    ans.append(heapq.heappop(h))
print(ans[-1])