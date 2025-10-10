def solution(array, commands):
    answer = []
    
    for i, j, k in commands :
        arr = array[i-1:j]
        s_arr = sorted(arr)
        answer.append(s_arr[k-1])
    return answer