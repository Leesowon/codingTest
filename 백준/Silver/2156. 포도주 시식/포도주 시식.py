import sys
input = sys.stdin.readline

n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]

dp[0] = wine[0]

if n > 1 :
    dp[1] = wine[0] + wine[1] # 당연히 다 마셔야..

if n > 2 : # 최소 3잔이면, 연속되지 않게 경우의 수 체크
    # 3번째 잔에 대해
    # o x o
    # x o o
    # o o x
    dp[2] = max((wine[0] + wine[2]), (wine[1] + wine[2]), dp[1])

    # o o x o
    # o x o o
    # ? o o x
    for i in range(3, n) :
        dp[i] = max((dp[i-2]+wine[i]), (dp[i-3]+wine[i-1]+wine[i]), dp[i-1])

# print(dp)
print(dp[n-1])