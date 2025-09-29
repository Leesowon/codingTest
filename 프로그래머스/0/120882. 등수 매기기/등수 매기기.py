def solution(score):
    answer = []
    
    avg = [sum(i)/2 for i in score]
    s_avg = sorted(avg, reverse=True) # 큰 평균부터 정렬
    
    for i in avg :
        answer.append(s_avg.index(i)+1)
        
    return answer