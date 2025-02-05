import sys
input = sys.stdin.readline

n,m = map(int, input().split())
forest = []
for _ in range(n) :
    forest.append(list(map(int, input().split())))


attack = [list(map(int, input().split())) for _ in range(2)]

for s,e in attack :
     check = [i for i in range(s-1,e)]
     for c in range(m) :
         for r in range(n) :
             if forest[r][c] == 1 and r in check :
                 check.remove(r)
                 forest[r][c] = 0

cnt = 0
for i in range(n) :
    for j in range(m) :
        if forest[i][j] == 1 :
            cnt += 1

print(cnt)