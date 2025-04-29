import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n) :
    coins.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1 # 원을 고르는 경우의 수는 1가지 (nC0)

for coin in coins : # 각 동전의 가치로 만들 수 있는 k금액
    for i in range(coin, k+1) :
        dp[i] = dp[i] + dp[i-coin]
        # i원을 만들 수 있는 경우의 수
        # i-coin 현재에서 coin만큼 빠졌을 때의 경우의 수
        # i-coin 만큼 빠졌을 때의 경우의 수에 coin이 대신 들어가면 그 경우의 수가 새로운 coin가치를 포함하여 구하는 경우의 수
        # dp[i] : 이전 코인으로만 만들 수 있던 경우의 수

print(dp[k])