import sys
input = sys.stdin.readline
import heapq

n = int(input())
bundle = [int(input()) for _ in range(n)]
heapq.heapify(bundle)
ans = 0

# 이전에 더한거 누적 + 새로 합
while len(bundle) > 1: # 2개 남았을 때까지
    min_1 = heapq.heappop(bundle)
    min_2 = heapq.heappop(bundle)
    ans += min_1+min_2
    heapq.heappush(bundle, (min_1+min_2))

print(ans)