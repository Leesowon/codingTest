from collections import deque

def solution(priorities, location):
    answer = 0
    
    d = deque()
    # 중요도
    im = deque(sorted(priorities, reverse=True))
    
    for idx, value in enumerate(priorities) :
        d.append([idx, value])
    
    while d :
        # 1. 큐에서 꺼내기
        idx, value = d.popleft()
        
        if value < im[0] :
            d.append([idx, value])
            continue
        
#         is_next = False
#         # 2. 꺼낸 수보다 더 큰 수가 priorities에 있는지 확인
#         for i in range(len(d)) : 
#             ch_idx, ch_value = d[i]
            
#             # 2-1. 있다면 다시 큐에 넣기
#             if ch_value > value :
#                 d.append([idx, value])
#                 is_next = True
        
#         if is_next :
#             continue
        
        # 2-2. 없으면 실행
        answer += 1
        im.popleft()
        
        # 이게 location 이면 answer = now 끝
        if idx == location :
            return answer