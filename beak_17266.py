import sys
input = sys.stdin.readline

n = int(input()) # 시작 위치 0, 끝 위치 n-1
m = int(input())
x = list(map(int, input().split()))

# 가로등 사이 거리 중 최장거리 찾기
longest = 0
for i in range(len(x)-1) :
    longest = max(longest, (x[i+1]-x[i]))

ans = max(x[0], (longest+1)//2, n-x[-1])
print(ans)