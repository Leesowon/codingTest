import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
heap = []

for _ in range(n) :
    num = int(input())

    if num == 0 :
        if len(heap) == 0 : print(0)
        else :
            print(hq.heappop(heap))
    else :
        hq.heappush(heap, num)