def solution(my_string):
    answer = ''
    li = sorted(list(my_string.lower()))
    return ''.join(map(str, li))