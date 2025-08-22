def solution(emergency):
    sort = sorted(emergency, reverse=True)
    print(sort)
    return [sort.index(i) + 1 for i in emergency]