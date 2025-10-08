import heapq as hq

def solution(scoville, K):
    answer = 0
    
    h = []
    for sc in scoville :
        hq.heappush(h, sc)
    
    con = True
    while con :
        # 모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우
        # len(h) == 1 인데, k가 넘지 않을 경우
        
        # 제일 작은게 K 이상이면 끝
        f1 = hq.heappop(h)
        if f1 >= K :
            con = False
            continue
        
        if len(h) == 0 :
            return -1
        
        f2 = hq.heappop(h)
        
        hq.heappush(h, (f1 + 2*f2))
        answer += 1
    
    return answer