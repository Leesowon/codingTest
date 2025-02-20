import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
heap = []

for _ in range(n) :
    x = int(input())
    # x가 0이라면
    if x == 0 :
        # 배열이 비어있지 않으면 가장 작은 값 출력
        if heap :
            print(hq.heappop(heap))
        else :
            print(0)
    elif x > 0 and int(x) == x: # x가 자연수라면
        hq.heappush(heap, x)