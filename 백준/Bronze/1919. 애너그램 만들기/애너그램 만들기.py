import sys
input = sys.stdin.readline

w1 = list(input().strip())
w2 = list(input().strip())
w2_cp = w2.copy()

cnt = 0
for w in w1 :
    if w in w2_cp :
        cnt +=1
        w2_cp.remove(w)

ans = len(w1) + len(w2) - 2*cnt
print(ans)