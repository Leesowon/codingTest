import sys
input = sys.stdin.readline

x = int(input())
dp = [0 for _ in range(x+1)]

for i in range(2, x+1) :
    dp[i] = dp[i-1] + 1
    # i-1에서 1로 가기 위한 최소 연산 횟수 : dp[i-1]
    # i-1에서 i로 만들기 위해 연산을 한 번 수행

    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1) # -1 이랑 //2 비교
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[x])
