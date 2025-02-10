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
# def func3(g, h, w) : # 6 8 -> 8 6
#     res = [[0] * h for _ in range(w)]
#     for i in range(w) : # 6
#         for j in range(h) : # 8
#             res[i][j] = g[h-1-j][i]
#     return res

def func3(g) :
    w = len(g) # 세로 길이 -> 가로
    h = len(g[0]) # 가로 길이 -> 세로
    res = [[0] * w for _ in range(h)]

    for i in range(w) : # 원래 배열 a는 w가 세로였기 때문에 w를 먼저 돌아야 한다.
        for j in range(h) :
            res[j][w-i-1] = g[i][j]

    return res

# 왼쪽으로 90도 회전
# def func4(g, h, w) :
#     res = [[0] * h for _ in range(w)]
#     for i in range(w) :
#         for j in range(h) :
#             res[i][j] = g[j][w - 1 - i]
#     return res

def func4(g) :
    m = len(g) # 세로 길이 -> 가로
    n = len(g[0]) # 가로 길이 -> 세로
    res = [[0] * m for _ in range(n)]

    for i in range(m) :
        for j in range (n) :
            res[n-j-1][i] = g[i][j]

    return res

def func5(g, h, w) :
    res = [[0] * w for _ in range(h)]

    # 1 -> 2
    for i in range(h//2) :
        for j in range(w//2) :
            res[i][j+ w//2] = g[i][j]

    # 2 -> 3
    for i in range(h//2) :
        for j in range(w//2, w) :
            res[i+h//2][j] = g[i][j]

    # 3 -> 4
    for i in range(h//2, h) :
        for j in range(w//2, w) :
            res[i][j-w//2] = g[i][j]

    for i in range(h//2, h) :
        for j in range(w//2) :
            res[i-h//2][j] = g[i][j]
    return res

def func6(g, h, w) :
    res = [[0] * w for _ in range(h)]

    # 1 -> 4
    for i in range(h // 2):
        for j in range(w // 2):
            res[i + h//2][j] = g[i][j]

    # 2 -> 1
    for i in range(h // 2):
        for j in range(w // 2, w):
            res[i][j - w//2] = g[i][j]

    # 3 -> 2
    for i in range(h // 2, h):
        for j in range(w // 2, w):
            res[i - h//2][j] = g[i][j]

    # 4 -> 3
    for i in range(h // 2, h):
        for j in range(w // 2):
            res[i][j + w//2] = g[i][j]

    return res

n, m, r = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
oper = list(map(int,input().split()))

for op in oper:
    if op == 1:
        g = func1(g, n)
    elif op == 2 :
        g = func2(g, n, m)
    elif op == 3 :
        g = func3(g) # 회전은 할 때마다 가로/세로 깅리가 바뀌어야 하니까 세로, 가로 길이를 주지 않는다.
    elif op == 4 :
        g = func4(g)
    elif op == 5 :
        g = func5(g, n, m)
    elif op == 6 :
        g = func6(g, n, m)

for i in range(len(g)) :
    for j in range(len(g[0])) :
        print(g[i][j], end=' ')
    print()