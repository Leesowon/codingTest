def solution(numbers):
    answer = 0
    total = 0
    for num in numbers :
        total += num
    answer = total / len(numbers)
    return answer