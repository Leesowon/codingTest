'''
플루이드 워샬
- 모든 노드로부터 다른 노드까지의 최단 거리를 찾는 알고리즘
- i에서 j까지 가는 최단 거리를 구할 때 i->j로 바로 가는 것보다, i->k->j로 가는 것이 최단 거리인 경우가 있다.
모든 경우를 찾아 최솟값을 찾는 알고리즘

1. 하나의 노드에서 다른 노드까지 바로 갈 수 있다면 : 최소 비용 저장
2. 갈 수 없는 경우 : INF 저장
3. 3중 for문을 통해 거쳐가는 정점을 설정한다.
    3-1. 해당 정점을 거쳐가는 비용이 줄어든다 -> 최소 비용으로 교체
4. 반복하면서 최단 경로를 탐색

# 거쳐가는 정점
for k in range(n) :
    # 시작 정점
    for i in range(n) :
        # 도착 정점
        for k in range(n):
'''

def solution(n, results):
    '''
    i번째 사람의 순위는 2가지 방법으로 결정할 수 있다.
    1. i번째 사람이 다른 사람과 n-1번 경기를 함
    2. 이미 순위가 결정된 사람과 싸워 나온 승패를 이용
    
    이는, 바로 알 수도 있고, 한 다리 거쳐서 알 수도 있다는 것 -> 플루이드 워샬
    일반적인 경우 거쳐가는 정점이 있을 때 비용이 더 적은지 확인하는 절차가 필요
    but 지금은 연결이 되어있는지만 확인하면 된다.
    '''
    ranks = [[0] * n for _ in range(n)]
    
    for win , lose in results :
        ranks[win-1][lose-1] = 1
        ranks[lose-1][win-1] = -1
    
    for k in range(n) :
        for i in range(n) :
            for j in range(n) :
                if i == j : continue # 대각선 방향 무시
                if ranks[i][j] != 0 : continue # 이미 값이 들어있는 경우
                if ranks[i][k] == 1 and ranks[k][j] == 1 :
                    ranks[i][j] = 1
                    ranks[j][i] = -1
    
    answer = 0
    
    for per in ranks :
        if per.count(0) == 1 :
            answer += 1
    
    return answer