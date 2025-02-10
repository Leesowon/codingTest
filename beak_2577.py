import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

mul_str = str(a*b*c)
ans = [0] * 10

for m in mul_str :
    m = int(m)
    ans[m] += 1

print('\n'.join(map(str, ans)))