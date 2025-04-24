import sys, heapq
input = sys.stdin.readline

leftHeap = [] # 최대힙
rightHeap = [] # 최소힙

n = int(input())
for _ in range(n) :
    num = int(input())

    # 왼쪽 힙을 우선으로 넣기
    if len(leftHeap) > len(rightHeap) :
        heapq.heappush(rightHeap, num)
    else :
        heapq.heappush(leftHeap, -num) # 최대힙

    # print(f"left : {leftHeap}, right : {rightHeap}")

    # leftHeap[0] <= rightHeap[0] 을 유지해야 하기 때문에
    # 만약 leftHeap[0] > rightHeap[0] 이되면 두 값 바꿔줘야 한다.
    if len(leftHeap) > 0 and len(rightHeap) > 0 :
        if -leftHeap[0] > rightHeap[0] :
            tmpL = - heapq.heappop(leftHeap)
            tmpR = heapq.heappop(rightHeap)

            heapq.heappush(leftHeap, -tmpR)
            heapq.heappush(rightHeap, tmpL)

    print(-leftHeap[0])