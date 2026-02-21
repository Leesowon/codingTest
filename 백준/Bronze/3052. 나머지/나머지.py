import sys
input = sys.stdin.readline

ans = set()

for _ in range(10) :
    num = int(input()) % 42
    ans.add(num)

print(len(ans))