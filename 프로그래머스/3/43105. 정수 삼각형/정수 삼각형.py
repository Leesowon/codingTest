def solution(triangle):
    answer = 0
    
    n = len(triangle)

    dp = [[0] * i for i in range(1, n+1)]
    
    dp[0][0] = triangle[0][0]
        
    for i in range(1, n) :
        for j in range(len(triangle[i])) :
            
            if j == 0 :
                dp[i][j] = triangle[i][j] + dp[i-1][j]
            elif j == i :
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
            else :
                dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    
    answer = max(dp[n-1])
    
    return answer