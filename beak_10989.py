import sys
input = sys.stdin.readline

arr = [0] * 10001 # 최대 10,000개의 수가 주어짐
n = int(input())

for _ in range(n) :
    idx = int(input())
    arr[idx] += 1

for i in range(len(arr)) :
    if arr[i] != 0 :
        for _ in range(arr[i]) :
            print(i)