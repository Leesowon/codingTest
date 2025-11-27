import sys
input = sys.stdin.readline

def merge_sort(s, e) :
    if s < e :
        m = (s + e) // 2
        merge_sort(s,m)
        merge_sort(m+1,e)
        merge(s,m,e)

def merge(s,m,e) :
    i = s
    j = m+1
    t = s

    while i <= m and j <= e :
        if arr[i] <= arr[j] :
            result.append(arr[i])
            tmp[t] = arr[i]
            t += 1
            i += 1
        else :
            result.append(arr[j])
            tmp[t] = arr[j]
            t += 1
            j += 1

    while i <= m :
        result.append(arr[i])
        tmp[t] = arr[i]
        t += 1
        i += 1

    while j <= e :
        result.append(arr[j])
        tmp[t] = arr[j]
        t += 1
        j += 1

    i = s
    t = s
    while i <= e :
        arr[i] = tmp[t]
        i += 1
        t += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = list(0 for _ in range(n))
result = list()
merge_sort(0, n-1)

if k <= len(result) :
    print(result[k-1])
else :
    print(-1)