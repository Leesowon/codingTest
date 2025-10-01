'''
코니는 매일 다른 옷을 조합하여 입는 것을 좋아한다.

- 각 종류별로 최대 한 개만 착용할 수 있다.
- 일부가 겹쳐도 완전 같지만 않다면 괜찮음
- 하루에 최대 한 개 이상 의상
- 서로 다른 조합의 수를 return


'''

from collections import Counter

def solution(clothes):
    answer = 1
    
    wear_hash = {}
    
    for cloth, kind in clothes :
        if kind in wear_hash :
            wear_hash[kind].append(cloth)
        else :
            wear_hash[kind] = [cloth]

    for kind in wear_hash :
        answer *= (len(wear_hash[kind])+1)
    
    return answer-1