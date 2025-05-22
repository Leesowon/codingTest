import sys
input = sys.stdin.readline

n = int(input())
score = []
for _ in range(n) :
    score.append(int(input()))

ans = 0
for i in range(n-1, 0, -1) :
    tmp = 0
    if score[i] <= score[i-1] :
        # print(f"i : {score[i]}, i-1 : {score[i-1]}")
        tmp = score[i]-1
        # print(f"tmp : {tmp}")
        ans += (score[i-1] - tmp)
        score[i-1] = tmp
        # print()

print(ans)
