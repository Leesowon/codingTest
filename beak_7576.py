import sys
input = sys.stdin.readline

from collections import deque

m, n = map(int, input().split())  # m : 가로, n : 세로
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))
day = 0

d = deque()
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

def isRipe(b) :
    for t in b :
        if 0 in t :
            return False
    return True

def bfs(dq):  # 1주변의 0 찾기
    h, w = dq.popleft()
    check = 0 # 1주변에 0이 있는지 확인

    for k in range(4):
        nh = h + dh[k]
        nw = w + dw[k]

        if nh < 0 or nh >= n or nw < 0 or nw >= m:
            continue
        if box[nh][nw] != 0:
            continue

        check += 1
        box[nh][nw] = 1

    if check == 0 : # 만약 1 주변에 0이 없으면 0 리턴
        return 0

    return 1

while True:
    # 종료조건1 : 모든 토마토가 익었을 때
    if isRipe(box):
        print(day)
        break
    # 종료조건2 : 모두 익지 못하는 상태

    # 1을 찾으면 bfs()에 넣어서 상하좌우 탐색
    ripe_tomato = []  # 새로 1 찾기
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                ripe_tomato.append((i, j))

    check = 0
    for t in ripe_tomato:
        d.append(t)
        check += bfs(d) # 상하좌우 탐색해서 1로 만들기

    if check == 0 :
        print(-1)
        break
    day += 1 # 1 주변 0을 다 1로 바꾸면 하루가 지남