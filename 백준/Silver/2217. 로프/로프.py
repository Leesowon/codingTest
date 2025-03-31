import sys
input = sys.stdin.readline

n = int(input())
rope = []
for _ in range(n) :
    rope.append(int(input()))
rope.sort(reverse=True)

dp = [0 for _ in range(n)]

dp[0] = rope[0]

for i in range(1, n) :
    dp[i] = max(dp[i-1], rope[i] * (i+1))

print(dp[n-1])