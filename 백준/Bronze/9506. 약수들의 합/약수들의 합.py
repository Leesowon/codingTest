import sys
input = sys.stdin.readline

while True :
    num = int(input())

    if num == -1 :
        break

    total = 0
    p = []
    for n in range(1, num // 2 + 1):
        if num % n == 0:
            total += n
            p.append(n)

    if total == num :
        print(f"{num} = {' + '.join(map(str, p))}")
    else :
        print(f"{num} is NOT perfect.")