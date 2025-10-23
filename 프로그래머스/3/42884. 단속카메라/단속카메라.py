def solution(routes):
    answer = 0
    
    # [진입, 진출]
    routes.sort(key = lambda x : x[1])
    # print(routes)
    
    # 현재 기준점
    key = -30001
    
    # 현재 기준점보다 다음 진입지점이 뒤에 있다면 cnt += 1
    for i in range(len(routes)):
        if key < routes[i][0] : 
            answer += 1
            key = routes[i][1]
    
    return answer