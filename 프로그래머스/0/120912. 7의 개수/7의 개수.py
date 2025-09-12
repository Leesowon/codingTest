def solution(array):
    answer = 0
    for arr in array :
        answer += str(arr).count('7')
    return answer