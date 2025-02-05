import sys
input = sys.stdin.readline

h, w, r, c = map(int, input().split())
def ans(a,b) :
    if a % (b+1) == 0 : # 배수이면
        return a//(b+1)
    return a//(b+1) + 1

print(ans(h,r) * ans(w,c))