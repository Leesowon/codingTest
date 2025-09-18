from itertools import permutations

def solution(dots):
    answer = 0
    
    # 인덱스 조합
    idx = [0, 1, 2, 3]
    for k in permutations(idx, 4) :
        i1, i2, i3, i4 = k
        
        # m1 = (dots[i1][1] - dots[i2][1]) / (dots[i1][0] - dots[i2][0])
        # m2 = (dots[i3][1] - dots[i4][1]) / (dots[i3][0] - dots[i4][0])
        
        if (dots[i1][1] - dots[i2][1]) * (dots[i3][0] - dots[i4][0]) == (dots[i3][1] - dots[i4][1]) * (dots[i1][0] - dots[i2][0]) :
            answer = 1
            break
        
    return answer