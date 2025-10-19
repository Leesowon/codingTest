from itertools import product

def solution(word):
    answer = 0
    
    w = ['A', 'E', 'I', 'O', 'U']
    dictionary = []
    
    for i in range(1, 6) :
        for r in product(w, repeat = i) :
            dictionary.append(''.join(r))
    
    dictionary.sort()
    
    answer = dictionary.index(word)+1
    
    return answer