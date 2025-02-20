import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for _ in range(n) :
    x = int(input())

    if x == 0 :
        if heap :
            # print(heapq.heappop(heap))
            abs_value, x_value = heapq.heappop(heap)
            print(x_value)
        else :
            print(0)
    else :
        heapq.heappush(heap, (abs(x), x))