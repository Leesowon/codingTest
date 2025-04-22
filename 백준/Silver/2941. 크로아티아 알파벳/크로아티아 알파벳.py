import sys
input = sys.stdin.readline

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().strip()

for c in cro :
    word = word.replace(c, '*')
print(len(word))