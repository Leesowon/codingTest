def solution(rsp):
    answer = ''
    for r in rsp :
        if r == "2" : # 가위
            answer += "0"
        elif r == "0" : # rock
            answer += "5"
        else : 
            answer += "2"
    return answer