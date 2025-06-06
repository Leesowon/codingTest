'''
약수의 개수가 1개이면 a**2
약수의 개수가 2개 이상이면 정렬해서 맨 처음 * 맨 끝
'''

n = int(input())
gcd = list(map(int, input().split()))

if n == 1 :
    print(gcd[0] ** 2)
else :
    gcd.sort()
    print(gcd[0] * gcd[-1])
