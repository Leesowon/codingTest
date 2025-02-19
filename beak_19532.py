import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())

x = (c*e - f*b) // (a*e - b*d)
y = (d*c - a*f) // (d*b - a*e)

print(x, y)