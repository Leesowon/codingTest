import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
words = sorted(list(input().split()))

vowel = ['a', 'e', 'i', 'o', 'u']
# vowel = 'aeiou'

def check(pw):
    cnt = 0
    for p in pw :
        if p in vowel:
            cnt += 1
    return cnt

ans = []
for w in combinations(words, l):
    pw = ''.join(w)
    if check(pw) > 0 and len(pw)-check(pw) > 1:
        # ans.append(pw)
        print(pw)