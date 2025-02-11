import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
taste = [list(map(int, input().split())) for _ in range(n)]

min_gap = float('inf')
for i in range(1, n+1) : # 1~n개까지 -> i
    for com in combinations(taste, i) : # 여러 재료 중 i개 선택
        sour = 1
        bitter = 0
        for k in range(len(com)): # 선택된 재료들의 신맛과 쓴맛의 차이 구하기
            s,b = com[k]
            sour *= s
            bitter += b
        min_gap = min(min_gap, abs(sour-bitter))
print(min_gap)