def solution(s1, s2):
    answer = 0
    # n(s1 교 s2) : n(s1) + n(s2) - n(s1 U s2)
    answer = len(s1) + len(s2) - len(set(s1+s2))
    return answer