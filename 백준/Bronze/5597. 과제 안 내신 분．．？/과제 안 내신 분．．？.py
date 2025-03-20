import sys
input = sys.stdin.readline

students = [int(input()) for _ in range(28)]
# students.sort()
ans = []

for i in range(1, 31) :
    if i not in students :
        ans.append(i)

ans.sort()
print('\n'.join(map(str, ans)))
