import sys
input = sys.stdin.readline
from collections import deque

# 1. 입력을 받아서 그래프로 저장
n = int(input())
arr = [[] for _ in range(n+1)] # 인접 리스트 : 노드 수만큼 배열 준비

for _ in range(n-1) : # 간선 정보를 읽어서 양방향 연결
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

# 2. bfs 탐색을 위한 큐를 만들고, 초기값 설정
now = 1 # 시작 노드
q = deque()
q.append(1) # 루트 노드를 큐에 넣음

parent = [0 for _ in range(n+1)] # 부모 노드 저장 배열
parent[1] = 1 # 루트 노드의 부모를 자기 자신으로 설정

# 3. bfs 탐색을 진행 한다. 방문 여부는 부모 노드가 설정 되었는지 여부로 한 번에 체크
while q :
    now = q.popleft() # 현재 노드
    for x in arr[now] : # 현재 노드와 연결된 노드 확인
        if parent[x] == 0 : # 아직 방문하지 않은 노드라면
            parent[x] = now # 부모 저장
            q.append(x) # 큐에 추가
for i in range(2, n+1) :
    print(parent[i])