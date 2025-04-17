n = int(input())

for i in range(1, n+1) : # 0
    for j in range(n, i, -1):
        print(' ', end='')
    print('*' * (i*2-1))

for i in range(1, n) : # i = 1,2,3,4
    for j in range(i) :
        print(' ', end='')
    print('*' * (n*2-(i*2+1)))