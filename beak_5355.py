import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    mars = list(input().split())
    num = float(mars[0])
    oper = mars[1:]

    for op in oper :
        if op == '@' :
            num *= 3
        elif op == '%' :
            num += 5
        elif op == '#' :
            num -= 7
    print("{:.2f}".format(num))