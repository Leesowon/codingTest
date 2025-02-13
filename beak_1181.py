import sys
input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

words = sorted(list(set(words)), key=lambda x : (len(x), x))
print('\n'.join(words))