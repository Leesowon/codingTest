import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
miro = [list(input()) for _ in range(n)]

INF = float('inf')
ans = INF

# 지훈이는 1분에 한 칸씩 상하좌우로 이동한다.
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 중복 방지를 위해
v = [[False] * m for _ in range(n)]

d = deque()
d_fire = deque()

# 처음 지훈/불의 위치 저장
for i in range(n):
    for j in range(m) :
        if miro[i][j] == 'J' :
            v[i][j] = True
            d.append((i, j)) # 지훈이의 위치와 시간
        if miro[i][j] == 'F' :
            d_fire.append((i, j))

# 1분당 불 번지기
def fire() :
    global n, m, miro, d_fire

    cnt_fire = len(d_fire)

    for _ in range(cnt_fire) :
        fr, fc = d_fire.popleft() # 체크한 거는 또 체크할 필요 없음

        for fk in range(4) :
            nfr = fr + dh[fk]
            nfc = fc + dw[fk]

            if 0 <= nfr < n and 0 <= nfc < m :
                if miro[nfr][nfc] != '#' and miro[nfr][nfc] != 'F' :
                    miro[nfr][nfc] = 'F'
                    d_fire.append((nfr, nfc)) # 다음번에 확산될 불씨

time = 0

while d : # 이동할 곳이 있는 동안
    time += 1

    # 1. 불 확산
    fire()

    # 2. 지훈이 1분 이동
    cnt_move = len(d)

    if cnt_move == 0 : # 불이 번졌는데 이동할 곳이 없다면 impossible
        print('IMPOSSIBLE')
        sys.exit(0)

    for _ in range(cnt_move) :
        r, c = d.popleft()

        for k in range(4) :
            nr = r + dh[k]
            nc = c + dw[k]

            # 3. 탈출 조건
            if not (0 <= nr < n and 0 <= nc < m) :
                print(time)
                sys.exit(0)

            # 4. 이동 조건
            if miro[nr][nc] == '.' and not v[nr][nc] :
                v[nr][nc] = True
                d.append((nr, nc))

# while 루프가 끝났다는 것은 자훈이가 더 이상 큐에 없음 -> 모두 갇힘
print('IMPOSSIBLE')