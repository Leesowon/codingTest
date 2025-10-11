from itertools import permutations

def solution(numbers):
    answer = ''
    
    # 숫자를 다 문자로 변환
    numbers = list(map(str, numbers))
    
    # 정렬
    numbers.sort(key=lambda x : x*3, reverse=True)
    
    answer = ''.join(numbers)
    
    return '0' if answer[0] == '0' else answer