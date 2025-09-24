import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

# 사과의 위치 - 시작이 1행 1열이라고 함
apples = set()
for _ in range(k) :
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

L = int(input()) # 뱀의 방향 변홧 횟수
moves= deque()
for _ in range(L) :
    t, di = input().split()
    moves.append((int(t), di))

snake = deque()
snake.append([0,0])
time = 0

# 방향: 우, 하, 좌, 상 (시계 방향)
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0  # 현재 방향 인덱스 (우)

while True :
    r, c = snake[-1] # 맨 앞
    dr, dc = dirs[d]

    # 머리 방향에 따라 한 칸 확장
    nr = r + dr
    nc = c + dc

    # 확장한 부분이 벽에 부딪히면 게임 끝
    if nr < 0 or nr >= n or nc < 0 or nc >= n :
        print(time+1)
        break

    # 뱀 몸에 닿아도 끝
    if [nr, nc] in snake:
        print(time + 1)
        break

    # 이동방향에 사과 없으면 꼬리 삭제 - 시작이 1행 1열이라고 함
    if (nr, nc) not in apples:
        snake.popleft()
    else : # 사과가 있는 칸으로 가면 사과 없어짐
        apples.remove((nr, nc))

    # 이동가능하면
    snake.append([nr, nc])
    time += 1

    if moves and moves[0][0] == time :
        _, turn = moves.popleft()
        if turn == 'D' : # 오른쪽 회전
            d = (d+1) % 4
        else :
            d = (d-1) % 4