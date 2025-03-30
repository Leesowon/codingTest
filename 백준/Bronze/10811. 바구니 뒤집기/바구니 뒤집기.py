import sys
input = sys.stdin.readline

n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

def rev(arr) :
    return arr[::-1]

for _ in range(m) :
    a,b = map(int,input().split())
    basket[a-1:b] = rev(basket[a-1:b])

print(' '.join(map(str, basket)))