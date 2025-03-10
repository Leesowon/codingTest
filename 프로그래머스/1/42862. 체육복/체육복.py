def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for re in reserve:
        if re in lost:  # 본인 먼저 확인
            lost.remove(re)
            continue
        elif (re - 1) in lost:
            lost.remove(re - 1)
            continue
        elif (re + 1) in lost:
            lost.remove(re + 1)
            continue

    return n - len(lost)

print(solution(5, [2,4], [1,3,5]))