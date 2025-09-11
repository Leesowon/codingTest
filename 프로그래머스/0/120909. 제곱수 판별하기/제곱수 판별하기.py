def solution(n):
    answer = 0
    for i in range(1, 1000001) :
        if i**2 == n :
            return 1
        if i**2 > n :
            return 2