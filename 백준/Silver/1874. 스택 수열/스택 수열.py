import sys
input = sys.stdin.readline

n = int(input())

nums = []
# 수열
for _ in range(n) :
    nums.append(int(input()))

stack = []
ans = []
for num in range(1, n+1) :
    # 우선 stack에 넣기
    stack.append(num)
    ans.append('+')

    # if len(stack) < 1:
    #     continue

    while len(stack) > 0 and nums[0] <= stack[-1] :
        del nums[0]
        stack.pop()
        ans.append('-')

if len(nums) == 0 :
    print('\n'.join(ans))
else :
    print('NO')