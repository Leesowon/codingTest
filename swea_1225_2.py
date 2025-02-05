import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    data = list(map(int, input().split()))

    def round(arr, a):
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[-1] = a

    cnt = [1,2,3,4,5]
    i = 0

    while True:
        if data[0] - cnt[i] <= 0 :
            round(data, 0)
            break
        else :
            data[0] = data[0] - cnt[i]
            round(data, data[0])
            i = (i+1) % 5


