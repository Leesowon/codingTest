import heapq as hq

def solution(operations):
    answer = [0, 0]
    
    min_h = [] # 최소 힙
    max_h = [] # 최대 힙
    
    for op in operations :
        w, num = op.split(' ')
        num = int(num)
        
        if w == 'I' :
            hq.heappush(min_h, num)
            hq.heappush(max_h, -num)
            
        else :
            # 빈 큐에 데이터를 삭제하라는 연산이 주어지면 해당 연산은 무시
            
            # 최솟값 삭제
            if num == -1 :
                if len(min_h) == 0 :
                    continue
                val = hq.heappop(min_h)
                max_h.remove(-val)
                hq.heapify(max_h)
            
            # 최댓값 삭제
            else : 
                if len(max_h) == 0 :
                    continue
                val = hq.heappop(max_h)
                min_h.remove(-val)
                hq.heapify(min_h)
        
    if len(min_h) > 0 :
        answer[1] = hq.heappop(min_h)

    if len(max_h) > 0 :
        answer[0] = -hq.heappop(max_h)
        
    return answer