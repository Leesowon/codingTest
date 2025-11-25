def solution(distance, rocks, n):
    answer = 0
    
    start = 1 # 커트라인 최솟값 : 1
    end = distance # 최댓값 : distance
    
    # 이분 탐색은 열이 정렬되어 있을 때만 가능하다.
    rocks.sort()
    rocks.append(distance)
    
    while start <= end :
        mid = (start + end) // 2
        
        # 제거하는 바위의 수
        cnt = 0
        # 이전 바위 위치
        previous = 0
        
        for rock in rocks :
            dist = rock - previous
            # 거리가 커트라인보다 작다면(현재 구하는건 최솟값 중 최댓값), 바위 제거    
            if dist < mid :
                cnt += 1
                # 제거한 바위가 너무 많다면 break
                if cnt > n :
                    break
            else : # 바위를 제거하지 않았다면
                previous = rock
        
        # 초과 제거한 경우 : 커트라인이 너무 높음
        if cnt > n :
            end = mid - 1
        # 이하 제거한 경우 : 커트라인이 적절하거나 너무 낮음
        else :
            answer = mid
            start = mid + 1
    return answer