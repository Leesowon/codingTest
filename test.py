
n = int(input())
m = int(input())
arr = {}

for i in range(m) :
    a,b,c = map(int, input().split())

    if a not in arr :
        arr[a] = []

    arr[a].append((b,c))

print(arr)