def solution(emergency):
    answer = []
    dic = {}
    
    # 크기순으로 정렬 후, 인덱스랑 묶어서
    # 해당 값의 인덱스가 뭔지 순서대로 answer에 저장
    
    emergency_sort = sorted(emergency, key = lambda x : -x)
    
    for idx, value in enumerate(emergency_sort) :
        # print(f"idx : {idx+1}, value : {value}")
        dic[value] = idx+1
    
    # print(dic)
    
    for e in emergency:
        # print("e :", e)
        # print(dic[e])
        answer.append(dic[e])
    
    return answer