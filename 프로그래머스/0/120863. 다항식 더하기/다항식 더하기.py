def solution(polynomial):
    answer = ''
    
    poly = polynomial.split(' ')
    x_num = 0 # x계수
    num = 0 # 그냥 자연수
    
    for i in range(len(poly)) :
        if 'x' in poly[i] :
            
            # 숫자랑 x를 분리해서 숫자만 더하기
            if poly[i] == 'x' : 
                poly[i] = '1x'
                
            n, st = poly[i].split('x')
            x_num += int(n)
            
        elif poly[i] != '+' :
            num += int(poly[i])
    
    if x_num == 0 and num != 0 :
        answer += str(num)
    elif x_num != 0 and num == 0 :
        if x_num == 1 :
            answer += 'x'
        else :
            answer += str(x_num) + 'x'
    else :
        if x_num == 1 :
            answer = 'x' + " + " + str(num)
        else :
            answer = str(x_num) + 'x' + " + " + str(num)
    
    return answer