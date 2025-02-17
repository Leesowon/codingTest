import sys
from itertools import combinations
input = sys.stdin.readline

h, w = map(int, input().split())
n = int(input())
stickers = [list(map(int, input().split())) for _ in range(n)]

def can_stick(s1, s2) :
    x1, y1 = s1
    x2, y2 = s2

    if x1+x2 <= h and y1+y2 <= w :
        return True
    if x1+x2 <= w and y1+y2 <= h :
        return True
    if x1+y2 <= h and x2+y1 <= w :
        return True
    if x1+y2 <= w and x2+y1 <= h :
        return True

    return False

# 스티커 2개 고르기
for sticker in combinations(stickers, 2) :
    s1, s2 = sticker
    if (s1, s2) :
