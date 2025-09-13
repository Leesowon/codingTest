def solution(dots):
    answer = 0
    row = 0
    col = 0
    
    # 점은 4개 - x값이 다른 좌표 2개, y값이 다른 좌표 2개
    for i in range(3) :
        if abs(dots[i][0] - dots[i+1][0]) != 0 :
            row = abs(dots[i][0] - dots[i+1][0])
        if abs(dots[i][1] - dots[i+1][1]) != 0 :
            col = abs(dots[i][1] - dots[i+1][1])
    
    return row * col