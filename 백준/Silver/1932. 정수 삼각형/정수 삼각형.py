import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] for _ in range(n)]

for i in range(n) :
    tri = list(map(int, input().split()))
    li = [0] * len(tri)
    dp[i] = li

    if i == 0 :
        dp[i][0] = tri[0]

    else :
        for j in range(len(tri)):
            if j == 0 :
                dp[i][j] = dp[i-1][0] + tri[j]
            elif j == len(tri)-1 :
                dp[i][j] = dp[i-1][j-1] + tri[j]
            else :
                dp[i][j] = tri[j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
