from collections import deque

def solution(people, limit):
    answer = 0
    
    people = deque(sorted(people))
    
    while people :
        if len(people) == 1 :
            answer += 1
            break
            
        heavy = people.pop()
        
        if people[0] + heavy <= limit :
            people.popleft()
        
        answer += 1
        
    return answer