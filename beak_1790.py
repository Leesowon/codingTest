import sys
input = sys.stdin.readline

cnt = [0, 0, 0] # -1, 1, 0

def check_same(paper, x, y, size) : # 모두 같은 영역에 있는지 확인
    first = paper[x][y]
    for i in range(x, x+size) :
        for j in range(y, y+size) :
            if paper[i][j] != first :
                return False
    return True

def cut(paper, x, y, size):
    if check_same(paper, x, y, size) : # 모든 값이 같다면 개수 증가 후 종료
        cnt[paper[x][y] + 1] += 1
        return

    # 9개로 자르기
    new_size = size // 3 # 새로운 크기 설정
    for i in range(3) :
        for j in range(3) :
            cut(paper, x+i*new_size, y+j*new_size, new_size)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cut(paper, 0, 0, n)

print(cnt[0])
print(cnt[2])
print(cnt[2])