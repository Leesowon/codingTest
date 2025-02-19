import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1) :
    num = list(str(i)) # 각 자리수 추출 -> 문자열 -> list
    # 각 자리가 str인 list의 값을 int로 바꿔서 합을 구하려고 한다.
    num_sum = sum(map(int, num))

    if n == (i+num_sum) :
        print(i)
        exit(0)

print(0)