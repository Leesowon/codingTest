def solution(genres, plays):
    answer = []
    
    # 각 장르별 총 재생횟수 저장
    count = {}
    for i in range(len(genres)) :
        if genres[i] in count :
            count[genres[i]] += plays[i]
        else :
            count[genres[i]] = plays[i]
    # print(f"장르별 재생 횟수 : {count}")
    
    # 많이 재생된 장르 정렬
    s_count = sorted(count.items(), key=lambda x : x[1], reverse = True)
    
    # print(f"s_count : {s_count}")
    
    albem = {}
    
    for i in range(len(genres)) :
        if genres[i] in albem :
            albem[genres[i]].append([plays[i], i])
        else :
            albem[genres[i]] = [[plays[i], i]]
    # print(albem)
    
    # 많이 재생된 장르별로 정렬
    for ge, pl in albem.items() :
        s_pl = sorted(pl, key=lambda x : (-x[0], x[1]))
        albem[ge] = s_pl
    
    # print(f"정렬 후 : {al}")
    
    # 각 장르별 재생횟수 큰 순서, idx 작은 순서로 정렬
    # 장르에 노래가 한 곡이라면 한 곡만 수록
    
    for genre, cnt in s_count :
        if len(albem[genre]) > 1 :
            for i in range(2) : # 장르별 2곡씩
                answer.append(albem[genre][i][1])
        else :
            answer.append(albem[genre][0][1])
    
    return answer