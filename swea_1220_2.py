import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    n = int(input()) # 정사각형 한 변의 길이
    table = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    for w in range(n) :
        for h in range(n) :
            check = 0
            if table[h][w] == 1:
                check = 1 # 이 전에 1이 있음을 표시
                # cnt += col(h,w,1)
                for k in range(h+1, n):
                    if table[k][w] == 2 and check == 1 :
                        cnt += 1
                        check = 0
                    if table[k][w] == 1 :
                        check = 1
                break # 더 이상 해당 h 줄에 대한 검사를 할 필요x
    print(f"#{tc} {cnt}")