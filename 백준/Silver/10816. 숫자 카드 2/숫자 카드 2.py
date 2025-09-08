import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

cards_set = {}
ans = []

for i in range(n) :
    if cards[i] in cards_set :
        cards_set[cards[i]] += 1
    else :
        cards_set[cards[i]] = 1

# print(f"card_set : {cards_set}")

for i in range(m) :
    # print(f"find[{i}] : {find[i]}")
    try :
        ans.append(cards_set[find[i]])
    except :
        ans.append(0)

print(' '.join(map(str, ans)))