import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1,11):
    n = int(input()) # 암호문 수
    # cy = list(map(int, input().split()))
    cy = input().split()
    com_num = int(input()) # 명령어 I,D,A의 개수
    commands = input().split()

    for i in range(len(commands)):
        if commands[i] == 'I':
            x = int(commands[i+1]) # x+1번째 부터 암호문 삽입
            y = int(commands[i+2])
            s = commands[i+3:i+3+y]

            cy = cy[:x] + s + cy[x:]

        if commands[i] == 'D':
            x = int(commands[i+1])
            y = int(commands[i+2])

            del cy[x:x+y]

        if commands[i] == 'A':
            y = int(commands[i+1])
            s = commands[i+2 : i+2+y]

            cy += s

    print(f"#{tc} {' '.join(cy[:10])}")


