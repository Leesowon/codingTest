import sys
input = sys.stdin.readline

n = int(input())
pro = sorted(list(map(int, input().split())))
x = int(input())

right = len(pro)-1
left = 0
ans = 0

while(left < right) :
    if pro[left] + pro[right] == x :
        ans += 1
        left += 1
        # right -= 1
    elif pro[left] + pro[right] < x :
        left += 1
    else :
        right -= 1
print(ans)