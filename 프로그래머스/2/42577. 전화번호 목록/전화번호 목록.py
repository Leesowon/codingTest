def solution(phone_book):
    answer = True
    
    hash = {}
    for ph in phone_book :
        hash[ph] = 1
    
    for phone in hash :
        tmp = ''
        for p in phone :
            tmp += p
            if tmp in hash and not tmp == phone : # 자기자신은 안됨
                answer = False
    return answer