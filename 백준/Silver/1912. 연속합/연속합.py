import sys
input = sys.stdin.readline

N = int(input())
prog = list(map(int, input().split()))

dp = [0] * N
dp[0] = prog[0]

if N > 1 :
    for i in range(1, N) :
        dp[i] = max(dp[i-1] + prog[i], prog[i])

print(max(dp))