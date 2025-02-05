import sys
sys.stdin = open("input.txt", "r")

tc = int(input())
for t in range(1, tc+1) :
    row, col = map(int, input().split())
    g = [list(input().strip()) for _ in range(row)]
    n = int(input())
    com = input()

    def isRange(h, w):
        if h < 0 or h >= row or w < 0 or w >= col :
            return False
        return True

    def shoot(h, w, dh, dw) :
        nh = h + dh
        nw = w + dw
        while isRange(nh, nw) :
            # 벽돌 벽에 충돌하면 평지로 바뀌고 소멸
            if g[nh][nw] == '*' :
                g[nh][nw] = '.'
                break
            # 강철 벽에 부딪히면 그냥 소멸
            elif g[nh][nw] == '#' :
                break

            nh += dh
            nw += dw

    # 1. 현재 전차의 위치 찾기
    current = None
    for i in range(row) :
        for j in range(col) :
            if g[i][j] == '^' or g[i][j] == 'v' or g[i][j] == '<' or g[i][j] == '>' :
            # if g[i][j] in '^v<>':
                current = (i,j)
                break
        if current :
            break

    # 2. 현재 명령어 확인 - 명령어 수 만큼 반복
    for c in com :
        h,w = current

        # 2-1. 만약 전차를 이동해야 한다면 -> 1) 전차가 다음 위치로 이동할 수 있는지 2) 명령어에 대한 방향 적용
        if c == 'U' : # up
            g[h][w] = '.'
            nh = h-1
            if isRange(nh, w) and g[nh][w] == '.': # 다음 위치로 이동할 수 있다면
                g[nh][w] = '^'
                # current.append((nh,w))
                h = nh
            else : # 이동할 수 없다면
                g[h][w] = '^'
                # current.append((h,w))
            current = (h,w)

        elif c == 'D' :
            g[h][w] = '.'
            nh = h + 1
            if isRange(nh, w) and g[nh][w] == '.':  # 다음 위치로 이동할 수 있다면
                g[nh][w] = 'v'
                # current.append((nh, w))
                h = nh
            else:  # 이동할 수 없다면
                g[h][w] = 'v'
                # current.append((h, w))
            current = (h, w)

        elif c == 'L' :
            g[h][w] = '.'
            nw = w - 1
            if isRange(h, nw) and g[h][nw] == '.':  # 다음 위치로 이동할 수 있다면
                g[h][nw] = '<'
                # current.append((h, nw))
                w = nw
            else:  # 이동할 수 없다면
                g[h][w] = '<'
                # current.append((h, w))
            current = (h, w)

        elif c == 'R':
            g[h][w] = '.'
            nw = w + 1
            if isRange(h, nw) and g[h][nw] == '.':  # 다음 위치로 이동할 수 있다면
                g[h][nw] = '>'
                # current.append((h, nw))
                w = nw
            else:  # 이동할 수 없다면
                g[h][w] = '>'
                # current.append((h, w))
            current = (h, w)

        else : # shoot
            # 현재 위치 h, w
            if g[h][w] == '^' :
                shoot(h,w,-1,0)

            elif g[h][w] == 'v' :
                shoot(h,w,+1,0)

            elif g[h][w] == '<' :
                shoot(h,w,0,-1)

            else :
                shoot(h, w, 0, 1)

            # current.append((h,w))
            current = (h, w)

    print(f'#{t}', end=' ')
    for line in g:
        print(''.join(line))
