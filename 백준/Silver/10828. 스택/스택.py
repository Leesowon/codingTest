import sys
input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n) :
    oper = list(input().split())

    if len(oper) == 2 :
        if oper[0] == 'push' :
            stack.append(oper[1])
    elif len(oper) == 1 :
        if oper[0] == 'pop' :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack.pop())
        elif oper[0] == 'size' :
            print(len(stack))
        elif oper[0] == 'empty' :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif oper[0] == 'top' :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack[-1])