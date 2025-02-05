import sys
input = sys.stdin.readline

# 집들의 1이상의 최소공약수
# 각 수의 약수를 구하고, 그 약수에 대한 인덱스 +1

n = int(input())
stove = list(map(int, input().split()))
idx = [0] * 100

def find_div(num) :
    check = 0
    for i in range(2, num//2+1) :
        if num % i == 0 :
            idx[i] += 1
            check = 1
    if check == 0 :
        idx[num] += 1

for s in stove :
    find_div(s)

min_value = float('inf')
for i in range(len(idx)) :
    if idx[i] > 0 and min_value > i :
        min_value = i

cnt = 0
for s in stove :
    if s % min_value == 0 :
        cnt += 1
print(cnt)