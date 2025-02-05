import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    r, str = input().split()

    for s in str :
        s = s * int(r)
        print(s, end='')
    print()