from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for order in permutations(dungeons, len(dungeons)) :
        labor = k # 노동..
        ans = 0
        for need, use in order :
            if labor < need :
                break
            labor -= use
            ans += 1
        answer = max(answer, ans)
    return answer