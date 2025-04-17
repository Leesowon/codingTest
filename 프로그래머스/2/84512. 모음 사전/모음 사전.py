import itertools

def solution(word):
    answer = 0
    
    vowel = ['A', 'E', 'I', 'O', 'U']
    words = []
    for i in range(1,6):
        for alp in itertools.combinations(vowel, i):
            alp_li = list(alp)
            
            for w in itertools.product(alp_li, repeat =i) :
                w = ''.join(map(str, w))
                if w in words :
                    continue
                words.append(w)
                    
    words = sorted(words)
    
    for idx in range(len(words)):
        if words[idx] == word :
            answer = idx + 1
            break
            
    
    return answer