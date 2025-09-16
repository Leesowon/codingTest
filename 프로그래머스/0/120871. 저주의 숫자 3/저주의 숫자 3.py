def solution(n):
    answer = 0
    town = []
    for i in range(300) :
        if '3' in str(i) :
            continue
        if i % 3 == 0 :
            continue
        town.append(i)
    return town[n-1]