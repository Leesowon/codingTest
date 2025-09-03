def solution(my_string):
    answer = ''
    al = ['a', 'e', 'i', 'o', 'u']
    for a in al :
        my_string = my_string.replace(a, '')
    return my_string