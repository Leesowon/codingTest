def solution(my_string):
    answer = ''
    # print(ord('A'))
    # print(ord('Z'))
    # print(ord('a'))
    # print(ord('z'))
    
    for s in my_string :
        
        if 65 <= ord(s) <= 90 :
            answer += s.lower()
            
        elif 97 <= ord(s) <= 122 :
            answer += s.upper()
    return answer