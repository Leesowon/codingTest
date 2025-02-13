import sys
input = sys.stdin.readline

n = int(input())
serial = [input().strip() for _ in range(n)]
nums = [str(i) for i in range(0,10)]
ans = []

# 알파벳 / 숫자 분리
def sep(astr) :
    alp = ''
    num = []
    for s in astr:
        if s in nums:
            num.append(int(s))
        else:
            alp += s
    if len(num) == 0 :
        return int(0)
    return sum(num)

# 3. 먼저 사전 순으로 정렬해두기
serial = sorted(serial)

# 1. 길이에 대하여 정렬
serial = sorted(serial,key = lambda x : len(x))

# 2. 같은 길이가 있는지 확인 -> 숫자의 합 오름차순
length = []
# 2-1. 길이들 체크
for s in serial :
    length.append(len(s))

# 2-2. 각 길이들의 갯수(key)에 대한 value 설정
len_dic = {}
len_set = sorted(list(set(length)))
for l in len_set :
    len_dic[l] = []
for s in serial :
    len_dic[len(s)].append(s)

# 2-3. 만약 특정 딕셔너리에 value의 개수가 1이 아니면 각 숫자들의 합을 기준으로 정렬
for l in len_set :
    if len(len_dic[l]) > 1 :
        len_dic[l] = sorted(len_dic[l], key=lambda x : sep(x))
        ans += len_dic[l]
    else :
        ans += len_dic[l]

print('\n'.join(ans))