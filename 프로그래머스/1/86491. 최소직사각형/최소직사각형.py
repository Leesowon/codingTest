def solution(sizes):
    answer = 0
    
    for size in sizes :
        size.sort()
    
    r = -float('inf')
    c = -float('inf')
    
    for row, col in sizes :
        r = max(row, r)
        c = max(col, c)
    
    answer = r*c
    
    return answer