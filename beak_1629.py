import sys
input = sys.stdin.read

def mul(a,b,c) :
    if b == 0 :
        return 1
    half = mul(a, b//2, c)
    half = (half * half) % c
    return (half * a) % c if b % 2 else half

a,b,c = map(int, input().split())
print(mul(a,b,c))