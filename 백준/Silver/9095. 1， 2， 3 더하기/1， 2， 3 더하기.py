import sys
input = sys.stdin.readline
from itertools import product, repeat

tc = int(input())

for _ in range(tc) :
    ans = 1
    n = int(input())

    nums = [1,2,3]

    for i in range(1, n) : # 1을 n번 더하는거 이상은 없음
        for res in product(nums, repeat=i) :
            if sum(res) == n :
                ans += 1
    print(ans)