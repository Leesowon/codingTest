import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
house = [list(input().strip()) for _ in range(n)]
v = [[False] * n for _ in range(n)]

dan = 0 # 총 단지 수
apts = [] # 아파트의 수를 저장할 배열

d = deque()
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]

# 1. 새로운 단지의 집 찾기 : 처음 시작하는 집은 한번도 방문하지 않은 집
for i in range(n) :
    for j in range(n) :
        if house[i][j] == '1' and not v[i][j] : # 1이면서 아직 방문하지 않은
            v[i][j] = True
            d.append((i,j))

            cnt_apt = 0 # 아파트 수 리셋
            while d:
                # 2. 해당 단지의 아파트 수 세기
                h, w = d.popleft()
                cnt_apt += 1

                for k in range(4) :
                    nh = h + dh[k]
                    nw = w + dw[k]

                    if nh < 0 or nh >= n or nw < 0 or nw >= n :
                        continue
                    if v[nh][nw]: # true : 이미 방문했다면
                        continue
                    if house[nh][nw] != '1' :
                        continue

                    # 해당 단지에 다른 집이 있다면
                    v[nh][nw] = True
                    d.append((nh,nw))

            apts.append(cnt_apt)
            dan += 1

print(dan)
print('\n'.join(map(str, sorted(apts))))