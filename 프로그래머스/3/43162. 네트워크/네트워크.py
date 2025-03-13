from collections import deque

def solution(n, computers):
    cnt = 0

    # dfs
    # stack : 선입후출
    # stack.append
    # stack.pop

    visited = [0] * n

    for i in range(n):
        # 현재 컴퓨터 & 아직 네트워크 연결을 확인하지 않았다면 stack에 넣기
        # -> 네트워크 연결 확인 시작 컴퓨터
        # stack에 넣는 순간 visited 처리

        stack = deque()

        if visited[i] != 1 and computers[i][i] == 1:
            stack.append(i)  # 현재 i번째 컴퓨터가 시작 컴퓨터로 들어있다.
            visited[i] = 1
            cnt += 1

            # i번째와 연결된 모든 컴퓨터 stack에 넣기
            # 연결된 컴퓨터가 있다면 & 아직 방문하지 않았다면
            # 해당 컴퓨터를 stack에 넣기
            if len(stack) == 0:
                break
                
            else:
                while stack:
                    cur_computer = stack.pop()
                    for j in range(n):
                        if visited[j] != 1 and computers[j][cur_computer] == 1:
                            stack.append(j)
                            visited[j] = 1

    return cnt