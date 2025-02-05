import sys
input = sys.stdin.readline

n,k = map(int, input().split())
temp = list(map(int, input().split()))

part_sum = sum(temp[:k])
ans = part_sum

for i in range(n-k) :
    part_sum += temp[i+k] - temp[i]
    if ans < part_sum :
        ans = part_sum

print(ans)