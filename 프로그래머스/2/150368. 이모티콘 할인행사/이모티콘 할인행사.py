def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    m = len(emoticons)
    
    best_join, best_sales = -1, -1
    rates = [0] * m # 각 이모티콘의 할인률을 담을 배열
    
    def dfs(i) :
        nonlocal best_join, best_sales
        
        if i == m :
            # 현재 rates 조합으로 가입/매출 계산
            join, sales = 0, 0
            
            for u_rate, u_price in users :
                total = 0
                
                for k in range(m) :
                    if rates[k] >= u_rate :
                        total += emoticons[k] * (100 - rates[k]) // 100
                        
                if total >= u_price :
                    join += 1
                else :
                    sales += total
            
            if join > best_join or (join == best_join and sales > best_sales) :
                best_join, best_sales = join, sales
            return
        
        # i번째 이모티콘의 할인률 선택
        for d in discounts :
            rates[i] = d
            dfs(i+1)
    
    dfs(0)
    return [best_join, best_sales]