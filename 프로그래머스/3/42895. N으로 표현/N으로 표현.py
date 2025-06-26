def solution(N, number):
    answer = -1
    
    dp = [set() for _ in range(9)] # 1~9
    
    for i in range(1, 9) :
        dp[i].add(int(str(N) * i))

    for i in range(1,9) :
        for j in range(i) :
            # 모든 사칙연산 조합
            for op1 in dp[j] :
                for op2 in dp[i-j] :
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0 :
                        dp[i].add(op1 // op2)
                    
        if number in dp[i] :
            answer = i
            break
    
    return answer