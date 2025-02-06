import sys
input = sys.stdin.readline

# 1번 연산. 상하 반전 (원래 그래프, 세로 길이)
def func1(g, h) :
    idx = 0
    while idx < h-idx-1:
        tmp = g[idx]
        g[idx] = g[h-idx-1]
        g[h-idx-1] = tmp
        idx += 1
    return g

# 2번 연산. 좌우 반전 (원래 그래프, 세로, 가로)
def func2(g, h, w) :
    for i in range(h) :
        idx = 0
        while idx < w-idx-1:
            tmp = g[i][idx]
            g[i][idx] = g[i][w - idx - 1]
            g[i][w - idx - 1] = tmp
            idx += 1
    return g

# 오른쪽으로 90도 회전 - 정사각형 / 직사각형
def func3(g, h, w) : # 6 8 -> 8 6
    res = [[0] * h for _ in range(w)]
    for i in range(h) : # 6
        for j in range(w) : # 8
            res[j][h-i-1] = g[i][j]
    return res

# 왼쪽으로 90도 회전
def func4(g, h, w) :
    res = [[0] * h for _ in range(w)]
    for i in range(h) :
        for j in range(w) :
            res[w-1-j][i] = g[i][j]
    return res

def func5(g, h, w) :
    res = [[0] * w for _ in range(h)]
    hm = h//2-1
    wm = w//2-1

    for i in range(h) :
        for j in range(w) :


    return

def func6(g, h, w) :
    return g


n, m, r = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
op = int(input())

for _ in range(r):
    if op == 1:
        g = func1(g, n)
    elif op == 2 :
        g = func2(g, n, m)
    elif op == 3 :
        g = func3(g, n, m)
    elif op == 4 :
        g = func4(g, n, m)
    elif op == 5 :
        g = func5(g, n, m)
    elif op == 6 :
        g = func5(g, n, m)


for i in range(len(g)) :
    for j in range(len(g[0])) :
        print(g[i][j], end=' ')
    print()