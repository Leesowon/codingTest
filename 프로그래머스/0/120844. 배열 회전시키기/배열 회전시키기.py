def solution(numbers, direction):
    answer = []
    if direction == "right" :
        tmp = numbers.pop()
        numbers.insert(0, tmp)
    else :
        tmp = numbers.pop(0)
        numbers.append(tmp)
    return numbers