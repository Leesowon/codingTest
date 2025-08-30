import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
for i in range(1, n+1) :
    name = input().rstrip()
    dic[i] = name
    dic[name] = i

for _ in range(m) :
    problem = input().strip()

    if problem.isdigit() :
        print(dic[int(problem)])

    else :
        print(dic[problem])