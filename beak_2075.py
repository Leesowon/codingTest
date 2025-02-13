import sys
input = sys.stdin.readline
import heapq

n = int(input())
h = []
for i in range(n) :
    num_list = list(map(int, input().split()))
    if not h : # h에 값이 없으면
        for num in num_list :
            heapq.heappush(h, num)
    else : # 값이 있으면 항상 h의 길이를 n으로 유지
        for num in num_list :
            if h[0] < num : # 현재 힙의 최솟값보다 현재 숫자가 더 클 경우, 큰 수가 바뀌어야 한다.
                heapq.heappush(h, num)
                heapq.heappop(h)

print(h[0]) # 5번째 큰 수부터 가장 큰 수까지 힙에 담겨잇음

