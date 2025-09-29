from collections import Counter

def solution(nums):
    answer = 0
    
    dic = Counter(nums) # 존재하는 총 포켓몬 수
    
    # 종류가 중요하지, 각 종류에 대한 마릿수는 중요하지 않음
    # 가져가려는 수가 종류보다 많다면, 모든 종류를 다 한마리씩은 데려갈 수 있음 -> len(dic)
    # 반면 가져가려는 수보다 종류가 많다면, 그러면 어떤 경우든 다 데려갈 수 있음
    if (len(nums) // 2) <= len(dic) :
        answer = len(nums)//2
    else :
        answer = len(dic)
    
    return answer