def solution(num, k):
    answer = -1
    
    sk = str(k)
    snum = str(num)
    
    if sk in snum :
        answer = snum.index(sk) + 1
    return answer