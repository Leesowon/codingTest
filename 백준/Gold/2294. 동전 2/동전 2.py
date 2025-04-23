import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n) :
    coin.append(int(input()))

INF = 1e9
dp = [INF for _ in range(k+1)]
dp[0] = 0

for c in coin :
    for i in range(c, k+1) :
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[k] == INF :
    print(-1)
else :
    print(dp[k])