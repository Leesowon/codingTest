import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc) :
    n = int(input())
    rank = list(map(int, input().split()))
    dic = {}

    # 6명이 안되는 팀 제거
    team = set(rank) # 몇 팀이 있는지 확인
    for t in team :
        if rank.count(t) != 6 : # 6명이 충족하지 않으면 제거
            while t in rank :
                rank.remove(t)

    # 각 팀 / 팀원에 대한 등수 입력
    for r in range(len(rank)) :
        if rank[r] not in dic.keys() : # 만약 아직 dic에 생성되지 않았으면 삭제
            dic[rank[r]] = []
        dic[rank[r]].append(r+1)

    winner = {} # team, score
    for k, v in dic.items():
        if len(winner) == 0 : # 아직 우승자가 없으면 처음 오는 팀이 우선 우승팀
            winner[k] = v
        else :
            if sum(winner[list(winner.keys())[0]][:4]) > sum(dic[k][:4]): # 더 작은게 이기는거
                del winner[list(winner.keys())[0]]
                winner[k] = v
            elif sum(winner[list(winner.keys())[0]][:4]) == sum(dic[k][:4]):
                winner_key = int(''.join(map(str, list(winner.keys()))))
                if dic[winner_key][4] > dic[k][4] :
                    del winner[list(winner.keys())[0]]
                    winner[k] = v
    print(int(''.join(map(str, list(winner.keys())))))