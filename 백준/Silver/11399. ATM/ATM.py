import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

total = 0

p.sort()

for i in range(1,n+1) :
    total += sum(p[:i])

print(total)