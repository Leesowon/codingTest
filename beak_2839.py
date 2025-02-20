import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement, combinations

n = int(input())
iter = [3, 5]
max_sugar = n//3 + 1

for sugar in range(1, max_sugar+1) :
    for k in combinations_with_replacement(iter, sugar) :
        if sum(k) == n :
            print(len(k))
            sys.exit(0)
print(-1)