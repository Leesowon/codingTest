from collections import deque

def solution(s):
    answer = 0
    li = s.split(' ')
    d = deque()
    
    for value in li :
        try :
            if (int(value)) == int(value) :
                d.append(int(value))
        except :
            d.pop()
            
    return sum(d)