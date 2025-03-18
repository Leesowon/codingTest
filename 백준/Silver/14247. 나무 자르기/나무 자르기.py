import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
growth = list(map(int, input().split()))

# 자라는 길이에 대해 정렬
trees = []
for i in range(n) :
    trees.append([growth[i], height[i]])

trees.sort() # 자라는 길이에 대해 정렬

ans = 0
# n-1 일부터 첫날까지
for i in range(n) :
    ans += trees[i][1] + trees[i][0] * i
print(ans)