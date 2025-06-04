import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = []

for c in combinations(arr, m) :
    # print(' '.join(map(str, c)))
    ans.append(c)

# ans.sort(key=lambda x : (x[0], x[1]))
for i in range(len(ans)) :
    print(' '.join(map(str, ans[i])))