import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int, input().split())))

m = int(input())
B = list(map(int, input().split()))

def two_point() :
    global A, B

    for num in B :

        # print(f"num : {num}")
        start = 0
        end = len(A)-1
        mid = (start + end) // 2

        while True :
            # print(f"mid : {mid}, start : {start}, end : {end}")
            mid = (start + end) // 2

            if mid < start or mid > end :
                print(0)
                break


            if num < A[mid] :
                end = mid-1
            if num > A[mid] :
                start = mid+1
            if num == A[mid] :
                print(1)
                break

two_point()