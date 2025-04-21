import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)] # r, g, b

INF = 1e9
dp_r = [INF for _ in range(n)]
dp_g = [INF for _ in range(n)]
dp_b = [INF for _ in range(n)]

dp_r[0] = cost[0][0]
dp_g[0] = cost[0][1]
dp_b[0] = cost[0][2]

for i in range(1, n) :
    dp_r[i] = min(dp_g[i-1], dp_b[i-1]) + cost[i][0]
    dp_g[i] = min(dp_r[i-1], dp_b[i-1]) + cost[i][1]
    dp_b[i] = min(dp_r[i-1], dp_g[i-1]) + cost[i][2]

print(min(dp_r[n-1], dp_g[n-1], dp_b[n-1]))