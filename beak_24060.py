import sys
input = sys.stdin.readline

def merge_sort(A, p, r) :
    if p < r :
        q = (p+r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

def merge(A, p, q, r) :
    global cnt, res
    l = p
    h = q+1
    tmp = []

    while l <= q and h <= r :
        if A[l] < A[h] :
            tmp.append(A[l])
            l += 1
        else :
            tmp.append(A[h])
            h += 1

    while l <= q : # 배열 왼쪽 부분이 남은 경우
        tmp.append(A[l])
        l += 1

    while h <= r : # 배열 오른쪽 부분이 남은 경우
        tmp.append(A[h])
        h += 1

    l = p
    t = 0

    while l <= r : # 결과를 A[p~r]에 저장
        A[l] = tmp[t]
        cnt += 1
        if cnt == k :
            res = A[l]
            break
        l += 1
        t += 1

n,k = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(A, 0, n-1)
print(res)