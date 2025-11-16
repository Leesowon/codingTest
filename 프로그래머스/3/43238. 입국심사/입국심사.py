'''
이분 탐색의 범위 : 심사를 하는데 총 걸리는 시간 -> 1분부터 가장 비효율적으로 심사를 받았을 때 걸리는 시간(분)
mid : 모든 심사관들에게 주어진 시간. -> people은 모든 심사관들이 mid분 동안 심사한 사람의 수
기준 : mid 동안 심사한 사람의 수(people)가 
    1. 심사 받아야할 사람의 수(n)보다 많거나 같을 경우에는 시간이 충분했던 것으로 주어진 시간을 줄리고 (right = mid-1)
    2. 심사 받아야 할 사감의 수(n) 보다 적은 경우에는 시간이 부족했던 것이므로 주어진 시간을 늘린다. (left = mid + 1)
'''

def solution(n, times):
    answer = 0
    
    left = 1
    right = max(times) * n
    
    while left <= right :
        mid = (left + right) // 2
        peo = 0 # 심사한 사람의 수
        
        for time in times :
            # peo 은 모든 심사관들이 mid 분 동안 심사한 사람의 수
            peo += mid // time

            # 모든 심사관을 거치지 않아도 Mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if peo >= n :
                break
                
        # 심사한 사람의 수가 심사 받아야할 수보다 많거나 같은 경우
        # 딱 n명 심사했더라도, 몇 분 시간이 남았을 수도 있으니 : 시간이 많을 수도 있다!
        if peo >= n :
            answer = mid
            right = mid-1
            
        # 심사한 사람의 수가 받아야 할 사람의 수보다 적은 경우
        elif peo < n : 
            left = mid + 1
            
    return answer