import sys
input = sys.stdin.readline
from itertools import combinations

def find_dis(house, chicks) :
    min_distance = float('inf')
    x, y = house
    # print('chicks : ', chicks)
    for i in range(len(chicks)) :
        cx, cy = chicks[i]
        min_distance = min(min_distance, (abs(x-cx) + abs(y-cy)))
    return min_distance

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
city_chick_distance = []

# 1. 치킨집들의 좌표 저장
before_chick = []
for r in range(n) :
    for c in range(n) :
        if city[r][c] == 2 :
            before_chick.append([r,c])

# 2. 전체에서 m개 선택 → 순서 x, 중복 x : 조합 (combinations)
after_chick = []
for i in combinations(before_chick, m) :
    after_chick.append(i) # 남겨질 m개씩 치킨집 조합

# 3. 모든 m개의 치킨집 조합에 대해 도시 치킨 거리 구하기 -> 최소 거리 찾기
for i in range(len(after_chick)) :
    # print('현재 m개의 치킨집 좌표 : ', after_chick[i])
    new_city = city # 폐업 후 도시

    # 원래 있던 치킨집이 새로운 조합 m개 안에 속하지 않는다면 폐업 (2->0)
    for b in before_chick :
        if b not in after_chick[i] :
            x, y = b
            new_city[x][y] = 0
    # print(new_city)

    # 4. 현재 남아있는 치킨집에 대한 도시 치킨 거리 구하기
    distance = []
    for r in range(n) :
        for c in range(n) :
            if new_city[r][c] == 1 : # 4-1. 집 찾기
                # 4-2. 집과 치킨집들 사이의 거리 구하기 : 그 중 짧은 치킨집이 해당 집의 치킨 거리
                distance.append(find_dis((r,c), after_chick[i]))

    city_chick_distance.append(sum(distance))

print(min(city_chick_distance))