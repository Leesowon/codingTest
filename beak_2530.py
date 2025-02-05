import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
d = int(input())

s += d
i = 0

while (True) :
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59 :
        break

    if s >= 3600 :
        h += s // 3600
        s -= 3600 * (s//3600)
    elif s >= 60 :
        m += s // 60
        s -= 60 * (s//60)
    elif m >= 60 :
        h += m//60
        m -= 60 * (m//60)
    elif h >= 24 :
        h = h % 24

print(h, m, s)