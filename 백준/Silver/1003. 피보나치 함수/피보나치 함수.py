import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    n = int(input())

    dp = [[0, 0] for _ in range(n+1)]

    dp[0] = [1, 0] # [0이 호출된 횟수, 1이 호출된 횟수]

    if n > 0 :
        dp[1] = [0, 1]

    if n > 1 :
        for i in range(2, n+1) :
            dp[i] = [x + y for x, y in zip(dp[i-1], dp[i-2])]

    print(' '.join(map(str, dp[n])))