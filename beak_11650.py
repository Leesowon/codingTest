import sys
input = sys.stdin.readline

n = int(input())
coordinates = [list(map(int, input().split())) for _ in range(n)]

coordinates = sorted(coordinates)
for c in coordinates :
    x, y = c
    print(x, y)