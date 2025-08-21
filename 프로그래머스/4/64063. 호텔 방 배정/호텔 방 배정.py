def solution(k, room_number):
    next_free = {}
    answer = []
    next_free
    
    for x in room_number :
        path = []
        # print(f"x : {x}")
        
        # 이미 배정된 방이면 계속 다음 방으로 이동
        while x in next_free :
            # print(f"next free x :{x}")
            path.append(x)
            x = next_free[x]
        
        # 원하던 방이 아직 배정되지 않았다면
        answer.append(x)
        next_free[x] = x+1
        
        # 경로 압축 : 지나온 방들은 한 번에 갱신 -> 원하는 방이 찼을 때 어느 방으로 배정될 것인가를 갱신
        for p in path:
            # print(f"path : {p}")
            next_free[p] = x + 1
        
    return answer