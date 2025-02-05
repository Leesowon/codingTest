import sys
input = sys.stdin.readline

n = int(input())

# 피보나치 재귀 호출
def fib(n, cnt_rev):
    cnt_rev += 1
    if (n == 1 or n == 2):
        return 1
    else :
        return fib(n-1) + fib(n-2)

# 피보나치 dp
def fibonacci(n, cnt_dp) :
    cnt_dp += 1
    if n <= 2 :
        return 1
    f = [0] * (n+1) # 0부터 n까지의 배열 생성
    f[1] = f[2] = 1
    for i in range(3, n+1) :
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib(n, 0)
fibonacci(n, 0)
