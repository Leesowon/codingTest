import sys
input = sys.stdin.readline

n = int(input())
wine = []
for _ in range(n) :
    wine.append(int(input()))

dp = [0 for _ in range(n)]
dp[0] = wine[0]
if n > 1 : # 최소 2잔 있음
    dp[1] = wine[0] + wine[1]

if n > 2 : # 최소 3잔 있음
    # 전전 + 현재 : w[0] + w[2]
    # 전 + 현재 : w[1] + w[2]
    # 전전 + 전 : w[0] + w[1]
    dp[2] = max((wine[0] + wine[2]) , (wine[1] + wine[2]), dp[1])

for i in range(3, n) :
    # 1. 현재의 잔을 마시는 경우
    # 1-1. 전전 마시고, 전 안마심 : dp[i-2] + wine[i]
    # 1-2. 전전 안마시고, 전 마심 : dp[i-3] + wine[i-1] + wine[i]

    # 2. 현재 잔을 안마시는 경우 : dp[i-1]

    dp[i] = max((dp[i-2] + wine[i]), (dp[i-3] + wine[i-1] + wine[i]), dp[i-1])

print(dp[n-1])