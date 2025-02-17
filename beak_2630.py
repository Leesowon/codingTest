import sys
input = sys.stdin.readline

cnt_w = 0 # 0 : 흰색
cnt_b = 0 # 1 : 파란색

def check_is_one_color(x, y, arr, side) : # x, y 종이 시작 좌표
    color = arr[x][y]
    for i in range(x, x+side) :
        for j in range(y, y+side) :
            if arr[i][j] != color:
                return False
    return True

def cut_paper(x, y, arr, side) :
    if check_is_one_color(x, y, arr, side) : # 한가지 색만 있다면
        global cnt_w, cnt_b
        if arr[x][y] == 0:
            cnt_w += 1
        else:
            cnt_b += 1
        return

    else :
        cut_n = side//2
        cut_paper(x, y, arr, cut_n)
        cut_paper(x+cut_n, y, arr, cut_n)
        cut_paper(x, y+cut_n, arr, cut_n)
        cut_paper(x+cut_n, y+cut_n, arr, cut_n)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cut_paper(0, 0, paper, n)
print(cnt_w)
print(cnt_b)