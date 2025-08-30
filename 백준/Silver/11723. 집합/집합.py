import sys
input = sys.stdin.readline

m = int(input())
s = set()

for _ in range(m):
    com = input().split()

    if com[0] == 'add':
        s.add(int(com[1]))
    elif com[0] == 'remove':
        s.discard(int(com[1]))
    elif com[0] == 'check':
        print(1 if int(com[1]) in s else 0)
    elif com[0] == 'toggle':
        x = int(com[1])
        if x in s: s.remove(x)
        else: s.add(x)
    elif com[0] == 'all':
        s = set(range(1, 21))
    elif com[0] == 'empty':
        s.clear()