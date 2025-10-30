def solution(arr):
    # 1. 숫자(nums)와 연산자(ops) 분리
    nums = []
    ops = []
    for item in arr:
        if item.isdigit():
            nums.append(int(item))
        else:
            ops.append(item)
    
    n = len(nums)
    
    # 2. DP 테이블 초기화
    # max_dp[i][j]: i부터 j까지의 연산 결과 최댓값
    # min_dp[i][j]: i부터 j까지의 연산 결과 최솟값
    # 계산 과정에서 비교를 위해 최댓값 테이블은 -무한대, 최솟값 테이블은 +무한대로 초기화
    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]

    # 3. 기본값(Base Case) 설정
    # 길이가 1인 구간(i == j)의 최댓값/최솟값은 자기 자신
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]

    # 4. DP 점화식 (핵심 로직)
    # length: 구간의 길이 (1부터 n-1까지. e.g., [0,1], [1,2]... -> [0, n-1])
    for length in range(1, n):
        # i: 구간의 시작 인덱스
        for i in range(n - length):
            j = i + length  # j: 구간의 끝 인덱스
            
            # k: 구간 [i, j]를 나누는 분할 지점 (i <= k < j)
            # (i ... k)  <연산자 k>  (k+1 ... j) 로 분할
            for k in range(i, j):
                op = ops[k] # k번째 연산자
                
                # [i, k] 구간의 최댓/최솟값
                left_max = max_dp[i][k]
                left_min = min_dp[i][k]
                
                # [k+1, j] 구간의 최댓/최솟값
                right_max = max_dp[k+1][j]
                right_min = min_dp[k+1][j]

                # k번째 연산자에 따라 [i, j]의 최댓/최솟값 갱신
                if op == '+':
                    # (최대) = (최대) + (최대)
                    max_dp[i][j] = max(max_dp[i][j], left_max + right_max)
                    # (최소) = (최소) + (최소)
                    min_dp[i][j] = min(min_dp[i][j], left_min + right_min)
                
                elif op == '-':
                    # (최대) = (최대) - (최소)  <- 핵심!
                    max_dp[i][j] = max(max_dp[i][j], left_max - right_min)
                    # (최소) = (최소) - (최대)  <- 핵심!
                    min_dp[i][j] = min(min_dp[i][j], left_min - right_max)

    # 5. 최종 결과 반환
    # 전체 구간 [0, n-1]의 최댓값
    return max_dp[0][n-1]