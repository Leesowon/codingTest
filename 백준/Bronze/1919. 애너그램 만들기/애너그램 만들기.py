import sys
input = sys.stdin.readline

w1 = list(input().strip())
w2 = list(input().strip())
cnt_w2 = w2.copy()

cnt = 0

for i in range(len(w1)):
    if w1[i] in cnt_w2 :
        cnt += 1
        cnt_w2.remove(w1[i])

print(len(w1) + len(w2) - cnt*2)