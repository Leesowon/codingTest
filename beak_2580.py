import sys
input = sys.stdin.readline

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []
for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            blank.append((i,j))

def check(r, c, ch_num) :
    # 가로, 세로
    for i in range(9) :
        if sudoku[r][i] == ch_num or sudoku[i][c] == ch_num :
            return False
    # 3x3
    x = (r//3) * 3
    y = (c//3) * 3
    for i in range(x, x+3) :
        for j in range(y, y+3) :
            if sudoku[i][j] == ch_num :
                return False
    return True

# def ch_row(r, ch_num) :
#     for i in range(9) :
#         if sudoku[r][i] == ch_num :
#             return False
#     return True
#
# def ch_col(c, ch_num) :
#     for i in range(9) :
#         if sudoku[i][c] == ch_num :
#             return False
#     return True
#
# def ch_rect(r, c, ch_num) :
#     x = (r//3) * 3
#     y = (c//3) * 3
#     for i in range(x, x+3) :
#         for j in range(y, y+3) :
#             if sudoku[i][j] == ch_num :
#                 return False
#     return True

# dfs & 백트래킹 : 한 칸씩 숫자를 채워가면서 유효한 경우만 탐색 - 불가능하면 되돌림
def dfs(n) :
    if n == len(blank) : # 모든 빈 칸을 다 채우면 종료
        # 스도쿠 안의 0이 더 이상 없으면
        for i in range(9) :
            print(' '.join(map(str, sudoku[i])))
        sys.exit(0)

    r,c = blank[n]
    for num in range(1,10) :
        if check(r, c, num) : # 가로, 세로, 3x3 통과
            sudoku[r][c] = num
            dfs(n+1)
            sudoku[r][c] = 0
dfs(0)