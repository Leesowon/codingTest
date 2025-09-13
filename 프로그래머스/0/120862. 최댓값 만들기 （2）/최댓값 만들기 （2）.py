def solution(numbers):
    answer = 0
    # 정렬을 해서 맨 앞 두 개 곱한거랑, 맨 뒤 두 개 곱한거 비교
    numbers = sorted(numbers)
    answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
    return answer