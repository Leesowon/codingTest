import sys
sys.stdin = open("input.txt", "r")

testcase = int(input())
for _ in range(testcase):
    h,w = map(int, input().split())
    g = [list(input()) for _ in range(h)]

    def find_high(arr, i, j):
        cnt = 0
        for j in range(h): # 첫 줄만 계산하면 되긴 함
            for i in range(w):
                if arr[i][j] == 1:
                    cnt+=1
            return cnt
            break # 까지 할 필요..?

    def make_code(arr, start_i, start_j, high): # 암호코드만 있는 리스트 생성
        code = []
        for i in range(start_i, 56):
            for j in range(start_j, high):
                code.append(g[i][j])
                return code

    def bin_to_int(arr) :
        n = 0
        for i in range(len(arr)):
            n += 2**i * int(arr[len(arr)-i-1])

    def int_arr(arr):
        int_list = []
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                int_list.append(arr[i][j:j+7])

    # 암호 코드 찾기
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 1 :
                high = find_high(g,i,j) # 암호코드가 저장된 세로 찾기
                pass_code = make_code(g, i, j, high) # 암호코드만 있는 리스트 생성
                int_arr(pass_code)



