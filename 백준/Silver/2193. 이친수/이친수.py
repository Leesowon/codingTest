import sys
input = sys.stdin.readline

N = int(input())

dp = [[0,0]] * (N+1) # [0으로 끝나는 수, 1로 끝나는 수]

dp[1] = [0, 1] # 1

if N > 1 :
    dp[2] = [1, 0] # 10

if N > 2 :
    for i in range(3, N+1) :
        dp[i] = [dp[i-1][0] + dp[i-1][1], dp[i-1][0]]

print(sum(dp[N]))