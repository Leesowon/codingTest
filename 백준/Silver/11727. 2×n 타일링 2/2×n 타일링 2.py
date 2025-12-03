import sys
input = sys.stdin.readline

n = int(input())

INF = 1e9
dp = [INF] * (n+1)

dp[0] = 0
dp[1] = 1

if n > 1 :
    dp[2] = 3

for i in range(3, n+1) :
    # i-1에 1x2 붙이기 (1가지) + i-2에 2x1 2개 or 2x2 1개 붙이기 (2가지)
    dp[i] = dp[i-2] * 2 + dp[i-1]

print(dp[n] % 10007)