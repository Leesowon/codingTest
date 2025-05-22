import sys
input = sys.stdin.readline

n = int(input())
workers = set()

for _ in range(n) :
    name, status = input().split()
    if status == 'enter' :
        workers.add(name)
    elif status == 'leave' and name in workers :
        # idx = workers.index(name)
        # del workers[idx]
        workers.remove(name)
        
sorted_workers = sorted(workers, reverse=True)
print('\n'.join(sorted_workers))