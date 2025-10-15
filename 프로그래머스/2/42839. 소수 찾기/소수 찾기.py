from itertools import permutations

def solution(numbers):
    answer = 0
    
    num_li = list(numbers)
    ans = set()
    
    for i in range(1, len(numbers)+1) :
        for num_p in permutations(num_li, i) : 
            ck = True
            num = int(''.join(num_p))
            
            if num > 1 :
                for j in range(2, num//2+1) :
                    if num % j == 0 :
                        ck = False
                        break

                if ck :
                    ans.add(num)
    
    return len(ans)