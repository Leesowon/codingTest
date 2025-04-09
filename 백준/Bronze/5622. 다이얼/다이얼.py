import sys
input = sys.stdin.readline

str_number = input().strip()
ans_sum = 0

for sn in str_number :
    if sn == 'A' or sn == 'B' or sn == 'C' :
        ans_sum += 3
    elif sn == 'D' or sn == 'E' or sn == 'F' :
        ans_sum += 4
    elif sn == 'G' or sn == 'H' or sn == 'I' :
        ans_sum += 5
    elif sn == 'J' or sn == 'K' or sn == 'L' :
        ans_sum += 6
    elif sn == 'M' or sn == 'N' or sn == 'O' :
        ans_sum += 7
    elif sn == 'P' or sn == 'Q' or sn == 'R' or sn == 'S':
        ans_sum += 8
    elif sn == 'T' or sn == 'U' or sn == 'V' :
        ans_sum += 9
    elif sn == 'W' or sn == 'X' or sn == 'Y' or sn == 'Z':
        ans_sum += 10
    else :
        ans_sum += 11

print(ans_sum)