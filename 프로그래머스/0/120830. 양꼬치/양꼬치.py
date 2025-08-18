def solution(n, k):
    answer = 0
    # 10인분 - n//10 만큼 뺀 나머지
    answer = n * 12000 + (k - n//10) * 2000
    return answer