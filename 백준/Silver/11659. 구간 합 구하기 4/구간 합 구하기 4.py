import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0] * (n+1)

dp[1] = arr[0]

if n > 1 :
    for i in range(1, n) : # O(N)
        dp[i+1] = dp[i] + arr[i]

for _ in range(m) : # O(m)
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])