def solution(genres, plays):
    answer = []
    
    # 1. [장르, 재생수, 고유번호] 형태의 리스트를 생성
    tmp = [[genres[i], plays[i], i] for i in range(len(genres))]
    
    # 2. 장르별로 정렬 -> 같은 장르끼리 모으고,
    #   재생수는 내림차순
    #   고유 번호는 오름차순 정렬
    tmp = sorted(tmp, key = lambda x : (x[0], -x[1], x[2]))
    
    # 3. 장르별 총 재생 횟수 딕셔너리를 생성
    total_genre_d = {}
    for g in tmp :
        if g[0] not in total_genre_d :
            total_genre_d[g[0]] = g[1]
        else :
            total_genre_d[g[0]] += g[1]
            
    # 4. 장르를 총 재생 횟수 기준으로 정렬(내림차순)
    total_genre_d = sorted(total_genre_d.items(), key = lambda x : -x[1])
    
    # 4. 각 장르별로 상위 2곡까지만 정답에 추가
    for i in total_genre_d : 
        cnt = 0
        for j in tmp :
            if i[0] == j[0] : # 장르가 같다면
                cnt += 1
                if cnt > 2 : 
                    break
                else :
                    answer.append(j[2]) # 고유 번호 추가
                    
    return answer