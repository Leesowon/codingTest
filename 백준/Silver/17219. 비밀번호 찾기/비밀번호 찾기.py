import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for _ in range(n) :
    site, pw = input().split(" ")
    dic[site] = pw.strip()

find = []
for _ in range(m) :
    find.append(input().strip())

for i in range(m):
    print(dic[find[i]])