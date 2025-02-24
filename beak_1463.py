import sys
input = sys.stdin.readline

def min_op(n) :
    dp = [0] * (n+1) # dp[i] : i를 1로 만들기 위한 최소 연산 횟수

    for i in range(2, n+1) :
        dp[i] = dp[i-1] + 1 # 1을 빼는 경우

        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1) # 2로 나누는 경우
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1) # 3으로 나누는 경우

    return dp[n]

n = int(input())
print(min_op(n))