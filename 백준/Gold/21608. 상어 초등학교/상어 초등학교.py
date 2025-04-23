import sys
input = sys.stdin.readline

dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 앉을 자리 찾기
# 1. 좋아하는 학생이 많은 자리

def dfs(studNum, like_stud) :
    global seat

    max_like = -1e9
    max_empty = -1e9
    change_seat = [] # r : 좋아하는 사람수, 빈자리

    # 앉을 칸 탐색
    for h in range(N) :
        for w in range(N) :
            if seat[h][w] != 0 : # 다른 학생이 이미 앉아있으면 Pass
                continue

            like = 0
            empty = 0
            # 앉을 수 있으면 주변 탐색
            for k in range(4) :
                nh = h + dh[k]
                nw = w + dw[k]

                if 0 <= nh < N and 0 <= nw < N :
                # 상하좌우 탐색하는데 좋아하는 친구가 있다면 like +1, 빈자리라면 empty+1
                    if seat[nh][nw] in like_stud :
                        like += 1
                    elif seat[nh][nw] == 0 :
                        empty += 1

            if max_like < like :
                change_seat = [h,w]
                max_like = like
                max_empty = empty # **
            elif max_like == like :
                if max_empty < empty :
                    change_seat = [h,w]
                    max_empty = empty

    ch, cw = change_seat
    seat[ch][cw] = studNum

N = int(input())
seat = [[0] * N for _ in range(N)]
like_info = [[] for _ in range(N**2)]

for _ in range(N**2) :
    ss = list(map(int, input().split()))
    studNum = ss[0]
    like_stud = ss[1:]
    dfs(studNum, like_stud)

    like_info[studNum-1] = like_stud

# 만족도 조사
ans = 0
for r in range(N) :
    for c in range(N) :
        # 해당 자리 학생이 좋아하는 학생들
        llike = like_info[seat[r][c]-1]
        cnt = 0
        # 주변에 좋아하는 사람 수
        for k in range(4) :
            nh = r + dh[k]
            nw = c + dw[k]

            if 0 <= nh < N and 0 <= nw < N:
                if seat[nh][nw] in llike :
                    cnt += 1
        # 만족도 update
        if cnt == 4 :
            ans += 1000
        elif cnt == 3 :
            ans += 100
        elif cnt == 2 :
            ans += 10
        elif cnt == 1 :
            ans += 1

print(ans)