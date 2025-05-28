import sys
input = sys.stdin.readline

n = int(input())

dp = [1e9 for _ in range(n+1)] # 각 거리에 대한 최소 이동 횟수
prev = [0 for _ in range(n+1)]

if n == 1 :
    dp[1] = 0

if n > 1 :
    for i in range(1, n+1) :
        if i % 6 == 0 :
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1

            if dp[i] == dp[i//3] + 1 :
                prev[i] = i // 3

            elif dp[i] == dp[i//2] + 1 :
                prev[i] = i // 2

            else :
                prev[i] = i-1

        elif i % 3 == 0 and dp[i//3] < dp[i-1] :
            dp[i] = dp[i//3] + 1
            prev[i] = i // 3

        elif i % 2 == 0 and dp[i//2] < dp[i-1] :
            dp[i] = dp[i//2] + 1
            prev[i] = i // 2

        else :
            dp[i] = dp[i-1] + 1
            prev[i] = i - 1

path = [n]
now = n

while now != 1 :
    path.append(prev[now])
    now = prev[now]

print(len(path)-1)
print(" ".join(map(str, path)))