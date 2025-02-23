import sys
input = sys.stdin.readline

n = int(input())
num = 1
ans = 1

while True :
    if n <= num :
        print(ans)
        break
    if ans == 1:
        num *= 6
    else :
        num += 6
    ans += 1