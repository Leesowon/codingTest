import sys
input = sys.stdin.readline

def mod(a,b,c) :
    if b == 1 :
        return a % c

    tmp = mod(a, b//2, c)

    if b % 2 == 0 :
        return (tmp * tmp) % c
    else :
        return ((tmp * tmp) % c) * a % c

a,b,c = map(int, input().split())
print(mod(a,b,c))
