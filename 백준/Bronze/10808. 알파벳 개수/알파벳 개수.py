import sys
input = sys.stdin.readline

string = input().strip()

arr = [0] * 26 # 0~25
for s in string :
    arr[ord(s)-97] += 1

for a in arr :
    print(a, end=' ')