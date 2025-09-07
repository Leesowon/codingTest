def solution(my_string, num1, num2):
    answer = ''
    word1 = my_string[num1]
    word2 = my_string[num2]
    
    answer = my_string[:num1] + word2 + my_string[num1+1 : num2] + word1 + my_string[num2+1:]
    return answer