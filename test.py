# 중복o, 순서 ㅐ : 중복 순열
from itertools import product, repeat

n, m = map(int, input().split())
iter = [i for i in range(1, n+1)]

for i in product(iter, repeat=m) :
    # arr = i
    print(' '.join(map(str, i)))