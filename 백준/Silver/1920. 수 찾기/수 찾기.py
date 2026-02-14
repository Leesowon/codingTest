import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split()))) # O(n log n)
m = int(input())
arr = list(map(int, input().split()))

start = 0
end = n-1

def findRes(A, value, start, end) :

    if start > end :
        print(0)
        return

    mid = (start + end) // 2

    if A[mid] == value :
        print(1)

    elif A[mid] > value :
        findRes(A, value, start, mid-1)

    elif A[mid] < value :
        findRes(A, value, mid+1, end)

for i in range(m) :
    findRes(A, arr[i], start, end)

