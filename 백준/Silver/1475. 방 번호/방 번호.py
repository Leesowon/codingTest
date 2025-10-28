import sys
input = sys.stdin.readline

number = input().strip()
num_li = [0] * 10 # 0~9
ck = 0

for num in number :
    if num == '6' or num == '9' :
        if ck == 0 : # 이미 6이나 9가 있음
            num_li[6] += 1
            ck = 1
        else :
            ck = 0
    else :
        num_li[int(num)] += 1

print(max(num_li))