import sys
input = sys.stdin.readline

while True :
    a,b,c = map(int, input().split())

    if a==b==c==0 :
        exit(0)

    l_side = -1e9

    if a < (b+c) and (a**2 == b**2 + c**2) :
        print("right")
    elif b < (a+c) and (b**2 == a**2 + c**2) :
        print("right")
    elif c < (a+b) and (c**2 == a**2 + b**2):
        print("right")
    else :
        print("wrong")
