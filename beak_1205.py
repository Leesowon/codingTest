import sys
input = sys.stdin.readline

n, s, p = map(int, input().split())
# n : 현재 랭킹에 있는 점수의 개수
# p : 랭킹에 등재될 수 있는 총 점수의 개수
# s : 내 노래 점수

if n == 0 :
    print(1)
    exit(0)

scores = list(map(int,input().split())) # len(scores) == n

# 랭킹 리스트가 다 찼다면
if len(scores) >= p :
    if min(scores) >= s :
        print(-1)
        exit(0)
    else :
        del scores[scores.index(min(scores))]
scores.append(s)
scores = sorted(scores, reverse=True)

# 랭킹 리스트에서 나의 랭킹 찾기 -> 동점자가 있어도 어차피 맨 앞의 인덱스를 출력하니까..
print(scores.index(s)+1)