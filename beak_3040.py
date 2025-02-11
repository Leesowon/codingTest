import sys
input = sys.stdin.readline
from itertools import combinations

num = [int(input()) for _ in range(9)]
ans = []

for i in combinations(num, 7) :
    if sum(i) == 100 :
        ans = list(i)
        break
print('\n'.join(map(str, ans)))