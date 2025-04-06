
a, b = input().split()
a_li = list(a)[::-1]
b_li = list(b)[::-1]

a_num = int(''.join(map(str, a_li)))
b_num = int(''.join(map(str, b_li)))

if a_num > b_num :
    print(a_num)
else :
    print(b_num)