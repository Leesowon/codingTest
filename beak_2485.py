import sys
input = sys.stdin.readline
import math

def func_gcd(a,b) :
    while b > 0:
        a,b = b, a%b
    return a

n = int(input())
cnt = 0

arr = sorted([int(input()) for _ in range(n)])

sub = []
# 1. 차이 구하기
for i in range(len(arr)-1) :
    sub.append(arr[i+1]-arr[i])

# 2. 최대 공약수 구하기
gcd = sub[0]
for i in range(1, len(sub)) :
    gcd = func_gcd(gcd, sub[i])

for j in sub :
    cnt += j//gcd -1

print(cnt)