import sys
input = sys.stdin.readline

n = int(input())
people = [list(input().split()) for _ in range(n)]

# people = sorted(people, key=lambda x : int(x[0]))
people.sort(key=lambda x : int(x[0]))

for age, name in people :
    print(age, name)