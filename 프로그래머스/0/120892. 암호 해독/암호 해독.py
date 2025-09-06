def solution(cipher, code):
    answer = ''
    # for i in range(code, len(cipher)+1, code) :
        # answer += cipher[i-1]
    answer = cipher[code-1::code]
    return answer