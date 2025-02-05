import sys
sys.stdin = open("input(1).txt", "r")

testcase = int(input())
for tc in range(testcase):
    num, c = map(int, input().split())
    num = list(str(num))
    cnt = 0

    def find_max(arr):
        max_idx = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] <= arr[j]:
                    max_idx = j
        return max_idx

    while cnt < c:
        for j in range(len(num)):
            # j 다음 가장 큰 값을 배열의 맨 뒤에서 부터 찾아야함
            # max_value = max(num[j:len(num)+1])
            # max_idx = num.index(max_value)
            max_idx = find_max(num[j:len(num)+1])
            if j != max_idx :
                tmp = num[j]
                num[j] = num[max_idx]
                num[max_idx] = tmp
            else : # 없으면 맨 뒤 바꾸기
                tmp = num[-1]
                num[-1] = num[-2]
                num[-2] = tmp
            break
        cnt += 1

    print(f"#{tc+1} {''.join(num)}")


