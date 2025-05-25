import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

lm = blocks[0]
rm = blocks[-1]

rain = 0

for i in range(1, w-1) :
    # 현재 위치 i에 대해 양 옆 가장 높은 위치 찾기
    lm = max(blocks[:i])
    rm = max(blocks[i+1:])

    # 더 낮은 높이에 대해 빗물이 쌓임
    com = min(lm, rm)

    if blocks[i] < com :
        rain += (com-blocks[i])

print(rain)