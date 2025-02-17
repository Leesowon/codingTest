import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
cnt = -1

def put_num(x, y, g) :
    global cnt, r, c
    for i in range(x, x+2) :
        for j in range(y, y+2) :
            cnt += 1
            g[i][j] = cnt
            if i == r and j == c :
                print(cnt)

def Z(x, y, g, side) :
    if side == 2 :
        put_num(x, y, g)
    else :
        new_n = side//2
        ## 방향 주의
        Z(x, y, g, new_n)
        Z(x, y+new_n, g, new_n)
        Z(x+new_n, y, g, new_n)
        Z(x+new_n, y+new_n, g, new_n)

Z(0, 0, g, 2**N)