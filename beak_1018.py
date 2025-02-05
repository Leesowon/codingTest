import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # m : 세로
board = []
for _ in range(n) :
    board.append(list(input().strip()))
result = []

for r in range(0, n-7) : # 세로 / 검사하는 체스판의 인덱스를 벗어나지 않게하기 위 해 -7
    for c in range(0, m-7): # 가로
        draw1 = 0 # 시작점이 흰색일 때 칠해야하는 갯수 계산
        draw2 = 0 # 시작점이 검은색일 때 ~

        for i in range(r, r+8) :
            for j in range(c, c+8) :
                if (i+j) % 2 == 0 :
                    if board[i][j] != 'B' : # 시작이 흰색
                        draw1 += 1
                    if board[i][j] != 'W' :
                        draw2 += 1
                else :
                    if board[i][j] != 'W' : # 시작이 흰색
                        draw1 += 1
                    if board[i][j] != 'B' :
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)
print(min(result))