from collections import deque

# 한 글자만 다른지 비교하는 메서드
def isDiffOne(word1, word2) :
    cnt = 0
    for idx in range(len(word1)) :
        if word1[idx] != word2[idx] :
            cnt += 1
        if cnt > 1 :
            return False
    return True
    

def solution(begin, target, words):
    answer = 0
    
    d = deque()
    v = [False for _ in range(len(words))]
    
    d. append((0, begin)) # 변환 수(Count), 현재 단어
    
    while d :
        cnt, now = d.popleft()
        
        if now == target :
            answer = cnt
            break
        
        # words list를 확인하면서
        for i in range(len(words)) :
            new_word = words[i]
            new_cnt = cnt
            
            # words 안의 단어와 현재 단어가 한 글자만 다르고,
            # 아직 방문하지 않았다면
            # 덱에 추가
            
            if isDiffOne(now, new_word) and not v[i] :
                print(f"append 성공")
                new_cnt += 1
                d.append((new_cnt, new_word))
                v[i] = True
    
    return answer