def solution(n, lost, reserve):
    answer = 0

    # 도난 = 여벌 거르기
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    
    # 빠른 탐색을 위해 정렬
    for re in sorted(set_reserve) :
        if (re-1) in set_lost :
            set_lost.remove(re-1)
        elif (re+1) in set_lost :
            set_lost.remove(re+1)
    
    return n - len(set_lost)