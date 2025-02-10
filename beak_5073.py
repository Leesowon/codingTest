import sys
input = sys.stdin.readline

while (True) :
    tri = list(map(int, input().split()))
    if 0 in tri :
        break
    tri = sorted(tri)
    # 삼각형이 아니면
    if tri[2] >= tri[0] + tri[1] :
        print("Invalid")
    # 정삼각형
    elif len(set(tri)) == 1:
        print('Equilateral')
    # 이등변 삼각형
    elif len(set(tri)) == 2:
        print("Isosceles")
    else :
        print("Scalene")