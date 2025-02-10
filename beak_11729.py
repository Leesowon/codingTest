import sys
input = sys.stdin.readline

n = int(input())
def hanoi(n, a, b, c) :
    if n == 1 :
        print(a,c)
    else :
        hanoi(n-1, a, b, c)
        print(a,c)
        hanoi(n-1, b, a, c)

sum = 2**n - 1
print(sum)

hanoi(n, 1, 2, 3)