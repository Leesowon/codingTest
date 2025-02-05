import sys
sys.stdin = open("input.txt", "r")

for testcase in range(1,11):
    n = int(input())
    ch = input().split()
    com_num = int(input())
    commands = input().split()

    def insert(arr, x, s):
        # arr = arr[:x+1] + s + arr[x+1:] 과 같이 코드를 작성하면 =(대입연산자)의 특성ㄷ 때문에 함수 안에서 arr이라는 새로운 객체가 생성됨
        arr = arr[:x] + s + arr[x:]
        return arr

    def delete(arr, x, y):
        del arr[x : x+y] # 인덱스 Vs 번째

    def add(arr, s) :
        # arr += s
        arr.extend(s) # append vs extend
        # append : 1개씩, extend : iterable한 항목들을 넣음

    for i in range(len(commands)) :
        if commands[i] == "I":
            x = int(commands[i+1])
            y = int(commands[i+2])
            s = commands[i+3 : i+3+y]
            ch = insert(ch, x, s)

        if commands[i] == "D":
            x = int(commands[i+1])
            y = int(commands[i+2])
            delete(ch, x, y)

        if commands[i] == "A":
            y = int(commands[i+1])
            s = commands[i+2:i+2+y]
            add(ch, s)

    ans = ' '.join(ch[:10])
    print(f"#{testcase} {ans}")
