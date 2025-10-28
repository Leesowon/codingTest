import sys
input = sys.stdin.readline

testcase = int(input())

for tc in range(testcase) :
    ans = ''

    str1, str2 = input().split()

    str1_li = sorted(list(str1))
    str2_li = sorted(list(str2))

    for i in range(len(str1_li)) :
        if str1_li[i] != str2_li[i] :
            ans = "Impossible"
            break
        else :
            ans = "Possible"

    print(ans)