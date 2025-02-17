import sys
input = sys.stdin.readline

'''
1. 같은 성별
2. 같은 학년
3. 최대 k명
조건에 맞게 모든 학생을 배정하기 위해 필요한 방의 개수 

입력
dic_man = {'학년' : 학생 수}
딕셔너리를 돌면서 학생 수//k 인데 이때 %k 가 0이 아니라면 +1
'''
n, k = map(int, input().split())

stu_boy = {}
stu_girl = {}

for _ in range(n) :
    s, g = map(int, input().split())
    if s == 0: # 남학생
        if g not in stu_boy.keys() : # 처음 학년
            stu_boy[g] = 1
        else :
            stu_boy[g] += 1
    else :
        if g not in stu_girl.keys() : # 처음 학년
            stu_girl[g] = 1
        else :
            stu_girl[g] += 1

cnt = 0
for grade, students in stu_boy.items() :
    if students % k != 0 :
        cnt += students//k + 1
    else :
        cnt += students // k

for grade, students in stu_girl.items() :
    if students % k != 0 :
        cnt += students//k + 1
    else :
        cnt += students // k

print(cnt)