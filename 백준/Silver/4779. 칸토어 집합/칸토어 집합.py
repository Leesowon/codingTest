import sys
input = sys.stdin.readline

def cut(n) : # a: 시작점
    if n == 1 :
        return '-'

    left = cut(n//3)
    center = ' ' * (n//3)
    return left + center + left

while True :
    try :
        n = int(input())
        result = cut(3**n)
        print(result)
        
    except :
        break
