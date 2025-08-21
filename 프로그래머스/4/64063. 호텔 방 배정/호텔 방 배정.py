# 재귀함수로 찾아가는 부분
# 값들간의 연결

# 파이썬은 재귀함수 횟수가 2000 밖에 안됨 -> 재귀함수를 많이 할 수 있도록 설정
import sys
sys.setrecursionlimit(10000)

def solution(k, room_number):
    answer = []
    
    parent = {} # 각 방 번호가 가르키는 '다음 가능한 빈 방 번호'를 저장하는 딕셔너리 - 빠른 검색은 dict가 최고!
    
    # union-find
    def find(x) :
        # x번 방이 비어있다면  (parent 기록이 없다면)
        # x번 방을 배정하고, 다음 가능한 방 번호를 parent[x]에 저장
        if x not in parent :
            parent[x] = x+1
            return x
        
        # 이미 배정된 방이라면, parent[x]가 가리키는 다음 방으로 이동하여 재귀적으로 다음 탐색
        # 이때, 경로 압축하여 중간 경로를 한번에 건더 뛸 수 있도록 설정
        parent[x] = find(parent[x])
        return parent[x]
        
    # 모든 고객들이 요청한 방 번호 순서대로 처리
    for room in room_number :
        assigned_room = find(room)
        answer.append(assigned_room)
        
    return answer