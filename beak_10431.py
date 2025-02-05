import sys
input = sys.stdin.readline

p = int(input())
for _ in range(p) :
    arr = list(map(int, input().split()))
    cnt = 0

    for i in range(len(arr)-1) :
        for j in range(i+1, len(arr)) : # i의 뒤에 있는 애들과 비교
            if arr[i] > arr[j] :
                arr[i], arr[j] = arr[j], arr[i]
                cnt += 1
    print(arr[0], cnt)