import sys
input = sys.stdin.readline

n, k = map(int, input().split())
table = list(input().strip())
cnt = 0

for i in range(len(table)) :
    if table[i] == 'P' :
        for j in range(i-k, i+k+1) :
            if j < 0 or j >= n : # 범위 넘으면
                continue
            if table[j] == 'H' :
                table[j] = 'eat'
                cnt += 1
                break
print(cnt)