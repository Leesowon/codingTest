import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting = sorted(meeting, key=lambda x : (x[1], x[0]))
ans = 0

# 다음 순서로 진행할 회의 찾기
cur_start, cur_end = 0, 0
for start, end in meeting :
    if cur_end <= start :
        cur_start = start
        cur_end = end
        ans += 1

print(ans)