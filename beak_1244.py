import sys
input = sys.stdin.readline

switch = int(input())
switch_state = list(map(int, input().split()))
stu_num = int(input())
students = [list(map(int, input().split())) for _ in range(stu_num)]

def change_switch(state) :
    # if state == 0 :
    #     return 1
    # return 0
    return 1-state

for g, n in students : # 받은 번호
    idx = n-1
    if g == 1 : # 남자

        # for i in range(switch) :
        #     if (i+1) % n == 0 :
        #         switch_state[i] = change_switch(switch_state[i])

        for i in range(idx, switch, n) : # 받은 번호의 배수만 처리
            switch_state[i] = change_switch(switch_state[i])

    else : # 여자
        cnt = 0
        while idx - cnt >= 0 and idx + cnt < switch:
            if switch_state[idx-cnt] == switch_state[idx+cnt] :
                cnt += 1
            else:
                break
        cnt -= 1  # 마지막 증가된 값을 조정
        for i in range(idx-cnt, idx+cnt+1) :
            switch_state[i] = change_switch(switch_state[i])

for i in range(len(switch_state)) :
    if i % 20 == 0 and i != 0 :
        print()
    print(switch_state[i], end=' ')

# 출력: 20개씩 나누어 출력
# for i in range(0, switch, 20):
#     print(' '.join(map(str, switch_state[i:i + 20])))