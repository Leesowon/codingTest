import sys
input = sys.stdin.readline

'''
N개의 시험장
각 시험장마다 Ai명의 응시자

총감독관 & 부감독관
- 총감독관 : 한 시험장에서 감시할 수 있는 응시자 수가 B명
- 부감독관 : 한 시험장에서 감시할 수 있는 응시자 수가 C명

한 시험장에 총감독관은 1명, 부 감독관은 여러명 가능
모든 응시생을 감시해야 할 때, 필요한 감독관의 수의 최솟값
'''

n = int(input())
applicant = list(map(int, input().split()))
inspector1, inspector2 = map(int, input().split())

cnt = 0
for app in applicant :
    cnt += 1 # 총감독관
    app -= inspector1

    # 몇명의 부감독관이 추가로 더 필요한가
    # 배수인가 아닌가
    if app > 0 :
        if app % inspector2 == 0 :
            cnt += app//inspector2
        else :
            cnt += app//inspector2 + 1

print(cnt)
