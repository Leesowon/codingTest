import sys
input = sys.stdin.readline

n = int(input())
g = []
for _ in range(n) :
    g.append(list(input()))

heart = ''
for i in range(n) :
    for j in range(n) :
        if g[i][j] == "*" :
            heart = (i+1,j)
            break
    if len(heart) != 0 :
        break

body = []
h,w = heart

def find_left_arm(h, w) :
    cnt = -1 # 처음은 심장
    while w >= 0 :
        if g[h][w] == "_" :
            return cnt
        else :
            w-= 1
            cnt += 1
    return cnt

def find_right_arm(h, w):
    cnt = -1
    while w < n :
        if g[h][w] == '_' :
            return cnt
        else :
            w += 1
            cnt += 1
    return cnt

def find_back(h, w) :
    cnt = -1 # 심장에서 시작
    while h < n :
        if g[h][w] == '_' :
            return cnt
        else :
            cnt += 1
            h += 1
    return cnt

def find_leg(h, w) :
    cnt = 0
    while h < n :
        if g[h][w] == '_' :
            return cnt
        else :
            cnt += 1
            h += 1
    return cnt

print(h+1,w+1) # 좌표가 1부터 시작
body.append(find_left_arm(h,w))
body.append(find_right_arm(h,w))
body.append(find_back(h,w))
back = body[-1]
body.append(find_leg(h+back+1, w-1))
body.append(find_leg(h+back+1, w+1))

print(' '.join(map(str, body)))