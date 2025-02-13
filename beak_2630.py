import sys
input = sys.stdin.readline

cnt_white = 0
cnt_blue = 0

# 한가지 색만 있는지 확인
def check_one(arr) :
    if 1 in arr :
        color = 1
    else :
        color = 0
    if abs(color-1) in arr :
        return False
    return True

def cut(arr, x, y, n) :
    global cnt_blue, cnt_white # 0

    if n == 1 or check_one(arr) : # 하나의 색만 있다면
        if 1 in arr :
            cnt_blue += 1
        else :
            cnt_white += 1
        return

    else :
        # 4개로 자르기
        new_size = n//2
        cut(arr, x, y, new_size)  # 좌상
        cut(arr, x, y + new_size, new_size)  # 우상
        cut(arr, x + new_size, y, new_size)  # 좌하
        cut(arr, x + new_size, y + new_size, new_size)  # 우하

n = int(input())
pArr = [list(map(int, input().split())) for _ in range(n)]

cut(pArr, 0, 0, n) # 배열, 시작 x, 시작 y, 크기
print(cnt_white)
print(cnt_blue)