import sys
input = sys.stdin.readline

k, l = map(int, input().split())
hak = {}

for i in range(l):
    num = input().strip()  # 문자열로 입력받기 (중요!)
    hak[num] = i  # 마지막 클릭 시점 저장

hak_sort = sorted(hak.items(), key=lambda x: x[1])

for i in range(min(k, len(hak_sort))):
    print(hak_sort[i][0])
