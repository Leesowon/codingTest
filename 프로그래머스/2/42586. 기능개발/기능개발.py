def solution(progresses, speeds):
    answer = []
    
    conti = True
    while conti :
        # 1. 작업 진도 나가기
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
        
        # 2. 앞에서 부터 100 이상인거 체크 및 배포되는 작업 갯수
        cnt = 0
        while len(progresses): 
            value = progresses.pop(0)
            
            if value < 100 :
                progresses.insert(0, value)
                break
            else :
                cnt += 1
                speeds.pop(0)
        
        if cnt > 0 :
            answer.append(cnt)
        if len(progresses) == 0 :
            break
    
    return answer