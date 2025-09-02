import sys
input = sys.stdin.readline

def cut(a, n) : # a: 시작점
    if n == 1 :
        return

    for i in range(a + (n//3), a + (n//3)*2) :
        result[i] = ' '
    cut(a, n//3) # 왼쪽 잘라내기
    cut(a + n//3*2, n//3) # 오른쪽 잘라내기

while True :
    try :
        n = int(input())
        result = ['-'] * (3**n)
        cut(0, 3**n)
        print(''.join(result))
    except :
        break
