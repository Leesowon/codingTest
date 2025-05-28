import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

# 순열
for c in permutations(nums, m) :
    print(' '.join(map(str, c)))