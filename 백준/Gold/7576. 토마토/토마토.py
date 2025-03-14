import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

d = deque()

# 이미 다 익어있다면 day = 0
# check = 0
# for i in range(n) :
#     if 0 not in box[i] :
#         check += 1
# if check == n :
#     print(0)
#     sys.exit(0)

# 우선 토마토 싹 다 넣기
for i in range(n) :
    for j in range(m) :
        if box[i][j] == 1 :
            d.append((i, j))

def dfs() :
    day = -1
    '''
    왜 day = -1로 시작?
        익은 토마토를 모두 덱에 넣어둔 상태에서 시작
        -> 첫번째 반복에서는 주변의 익지 않은 토마토에 대한 너비우선탐색을 하므로
        아무 변화도 없이 기존 익은 토마토만 처리
    '''
    while d :
        for _ in range(len(d)) :
            h, w = d.popleft() # 1 토마토를 기준으로

            # 상하좌우 안익은 토마토 덱에 넣기
            for k in range(4) :
                nh = h + dh[k]
                nw = w + dw[k]

                if (0<=nh<n and 0<=nw<m) and box[nh][nw] == 0 :
                    box[nh][nw] = 1
                    d.append((nh, nw))
        day += 1
    
    # 처음부터 다 익었다면 새로 append되지 않고 그냥 day += 1
    # 따라서 L13~20 부분을 따로 구현하지 않아도 된다.
    
    # 나왔는데 다 익지 못햇으면 -1
    for i in range(n) :
        if 0 in box[i] :
            day = -1
    
    return day

print(dfs())