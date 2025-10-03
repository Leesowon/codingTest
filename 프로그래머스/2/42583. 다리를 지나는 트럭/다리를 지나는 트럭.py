from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    total = 0
    
    while truck_weights:
        # truck = truck_weights.pop(0)
        truck = truck_weights.popleft()
        first = bridge.popleft() # 맨 앞 빼고 넣기
        total -= first
        
        # 넣을 수 있으면 넣고, 못넣으면 0
        # if sum(bridge) + truck <= weight :
        if total + truck <= weight : 
            bridge.append(truck)
            answer += 1
            total += truck
        # 넣을 수 없으면 결국 있는게 빠져야 함
        else :
            bridge.append(0)
            # truck_weights.insert(0, truck)
            truck_weights.appendleft(truck)
            answer += 1
    
    answer += bridge_length
    return answer