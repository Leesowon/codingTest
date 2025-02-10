import sys
input = sys.stdin.readline

# def isExist(n, arr) :
#     # 종료조건
#     if len(arr) == 1 and n not in arr :
#         return False
#
#     mid = len(arr) // 2
#     if n == arr[mid] :
#         return True
#
#     if n < arr[mid] :
#         return isExist(n, arr[:mid])
#     elif n >= arr[mid] :
#         return isExist(n, arr[mid:])

def isExist(n, arr):
    if not arr:  # 배열이 비었으면 False 반환
        return False

    mid = len(arr) // 2
    if n == arr[mid]:
        return True

    return isExist(n, arr[:mid]) if n < arr[mid] else isExist(n, arr[mid:])

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums = sorted(nums) # 정렬

ans = 0
for n in nums :
    if isExist(x-n, nums) :
        ans += 1
        del nums[nums.index(n)]
        del nums[nums.index(x-n)]

print(ans)