import heapq as hq

def solution(n, k, enemy):
    
    # 최대 힙
    max_heap = []
    
    for i in range(len(enemy)) :
        n -= enemy[i] # 일단 병사로 막음
        hq.heappush(max_heap, -enemy[i]) # 적의 수를 최대 힙에 넣음
        
        # 병사 수가 부족하면 지금까지 막은 것 중 가장 큰 공격을 무적권으로 바꾸기
        if n < 0 :
            if k > 0 :
                biggest = -hq.heappop(max_heap)
                n += biggest
                k -= 1
            else :
                return i
        
    # 다 막으면
    return len(enemy)