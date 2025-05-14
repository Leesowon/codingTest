import sys
input = sys.stdin.readline

'''
돌 1개 : 상근(1)
돌 2개 : 상근(1) 창영(1)
돌 3개 : 상근(3)
돌 4개 : 상근(3) 창영(1)
돌 5개 : 상근(3) 창영(1) 상근(1)
돌 6개 : 상근(3) 창영(3)
돌 7개 : 상근(3) 창영(3) 상근(1)
'''
n = int(input())

if n % 2 == 0 :
    print('CY')
else :
    print('SK')