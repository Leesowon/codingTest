import heapq as hq

def solution(jobs): # jobs : [작업이 요청되는 시점(req_time), 작업의 소요 시간(job_time)]
    jobs = sorted(jobs)
    answer = 0
    cur_time = 0 # 현재 시간
    
    q = [] # 대기 큐
    vq = [False] * len(jobs) # 대기큐에 들어갔는지 체크
    
    con = True
    while con :
        # 1. 현재 시간에 대해 요청이 들어온 작업을 대기큐에 넣기
        for idx, value in enumerate(jobs) :
            if vq[idx] :
                continue
                
            req_time, job_time = value
            
            # 현재 시간이 넘으면 break
            if req_time > cur_time :
                break
            
            # 대기큐에 들어 갈 수 있으면 : 작업 소요 시간이 짧은 것, 작업의 요청 시각이 빠른 것, 작업 번호가 작은 것 순서
            vq[idx] = True
            hq.heappush(q, [job_time, req_time, idx])
        
        # print(f"대기 큐  (작업 소요시간, 작업의 요청 시각, 작업 번호) : {q}")
        
        # 만약 대기큐가 비어있고, 
        if len(q) == 0 :
            # 아직 False가 vq에 남아있다면 시간 +=1
            if (False in vq) :
                cur_time += 1
            # 종료 조건
            else :
                con = False
            continue
        
        # 2. 우선순위가 가장 높은거 작업 -> 현재 시간 갱신
        jt, rt, i = hq.heappop(q)
        # print(f"작업 - idx : {i}, 작업 시간 : {jt}, 요청 시간 : {rt}")
        cur_time += jt
        answer += (cur_time - rt) # 작업 종료 시간 - 요청시간
        # print(f"작업 끝 : {answer}")
    
    return (answer // len(jobs))