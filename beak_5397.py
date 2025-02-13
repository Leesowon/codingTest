import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    keys = list(input().strip())
    cursor = 0
    ans = []

    for k in keys :
        if k == '<' :
            if cursor > 0 :
                cursor -= 1
        elif k == '>' :
            if cursor < len(ans) :
                cursor += 1
        elif k == '-' :
            if ans and cursor > 0 : # ans에 값이 있고 -
                del ans[cursor-1]
                cursor -= 1
        else :
            ans.insert(cursor, k)
            cursor += 1

    print(''.join(ans))