import sys
input = sys.stdin.readline

n, b = input().split()
b = int(b)
ans = 0

for idx, char in enumerate(reversed(n)) : # 문자를 뒤집어서 자릿수 처리
    if char.isdigit() :
        ans += int(char) * (b ** idx)
    else :
        ans += (ord(char) - 55) * (b ** idx)
print(ans)