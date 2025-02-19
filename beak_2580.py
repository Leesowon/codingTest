import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]

blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))

def check(r, c, ch_num): # 현재 0의 위치 & 체크할 숫자
    for i in range(9):
        if sudoku[r][i] == ch_num or sudoku[i][c] == ch_num:
            return False
    # 3x3
    x = (r // 3) * 3
    y = (c // 3) * 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if sudoku[i][j] == ch_num:
                return False
    return True

def dfs(n):
    if n == len(blank):  # 도든 0의 자리를 다 체크
        for i in range(9):  # 출력 및 종료
            print(' '.join(map(str, sudoku[i])))
        sys.exit(0)

    r, c = blank[n]  # 아직 다 체크하지 않았다면 현재
    for num in range(1, 10):
        if check(r, c, num):
            sudoku[r][c] = num  # 숫자를 채우고
            dfs(n + 1)  # 다음 칸으로 이동
            sudoku[r][c] = 0  # 선택한 숫자가 답이 아니라면 되돌리기 (0으로 원상복구) - 백트래킹

dfs(0)  # lo_zero[0] 부터 검사