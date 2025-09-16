from itertools import product

def solution(users, emoticons):
    answer = []
    
    discount = [10, 20, 30, 40] 
    
    # 각 이모티콘 할인률 조합 : dis_rate
    for dis_rate in product(discount, repeat = len(emoticons)) :
        
        buy, plus = 0, 0
        
        for rate, price in users :
            
            # 할인률을 적용한 모든 이모티콘 금액 합
            total_emoticons_price = 0
            
            for i in range(len(emoticons)) :
                # 유저의 할인률보다 더 할인한다면, 구매
                if dis_rate[i] >= rate :
                    total_emoticons_price += int((emoticons[i] * ((100-dis_rate[i])*0.01)))
                    
            # 플러스 가입
            if price <= total_emoticons_price :
                plus += 1
            else :
                buy += total_emoticons_price
        
        answer.append([plus, buy])
    
    answer.sort(key=lambda x : (x[0], x[1]), reverse=True)
    
    return answer[0]