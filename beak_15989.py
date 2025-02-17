import sys
from itertools import combinations_with_replacement as cr

input = sys.stdin.readline
tc = int(input())

for _ in range(tc) :
    cnt = 0
    n = int(input())
    iter = [1,2,3]

    for i in range(1, n) :
        for num in cr(iter, i) :
            if sum(num) == n :
                cnt += 1
    print(cnt+1)