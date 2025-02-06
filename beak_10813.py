import sys
input = sys.stdin.readline

n, m = map(int, input().split())
ball = [i for i in range(1,n+1)] # 1번부터 n번까지의 공
change = [list(map(int, input().split())) for _ in range(m)]

for a, b in change :
    tmp = ball[a-1]
    ball[a-1] = ball[b-1]
    ball[b-1] = tmp

print(' '.join(map(str, ball)))