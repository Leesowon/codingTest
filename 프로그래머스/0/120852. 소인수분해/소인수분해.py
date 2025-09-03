def solution(n):
    answer = []
    d = 2
    while n > 1 :
        if n % d == 0 :
            answer.append(d)
            n = n // d
        else :
            d += 1
    answer = sorted(list(set(answer)))
    return answer