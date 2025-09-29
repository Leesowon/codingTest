import collections

def solution(participant, completion):
    answer = ''
    
    # print(collections.Counter(participant))
    # print(collections.Counter(completion))
    
    # print(collections.Counter(participant) - collections.Counter(completion))
    
    answer = list(collections.Counter(participant) - collections.Counter(completion))
    
    return answer[0]