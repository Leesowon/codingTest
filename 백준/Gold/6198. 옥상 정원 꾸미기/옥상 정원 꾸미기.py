import sys
input = sys.stdin.readline

n = int(input())
roof = list(int(input()) for _ in range(n))

stack = []
ans = 0

for i in range(n) :
    while stack and stack[-1] <= roof[i] :
        stack.pop()
    ans += len(stack)
    stack.append(roof[i])

print(ans)