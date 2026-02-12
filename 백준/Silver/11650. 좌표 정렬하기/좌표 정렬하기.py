import sys
input = sys.stdin.readline

n = int(input())
dots = list()

for _ in range(n) :
    x, y = map(int, input().split())
    dots.append([x, y])

dots.sort(key = lambda x :(x[0], x[1]))
for i in range(n) :
    print(' '.join(map(str, dots[i])))