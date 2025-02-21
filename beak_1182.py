import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

def dfs(idx, total) :
    global ans
    if idx == n :
        if total == s :
            ans += 1
    dfs(idx+1, total)
    dfs(idx+1, total+arr[idx])

dfs(0,0) # 탐색 시작
if s == 0 :
    ans -= 1
print(ans)