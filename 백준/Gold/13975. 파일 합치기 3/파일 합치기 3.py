import sys
import heapq

def min_merge_cost(k, files):
    # 최소 힙에 파일 크기들 넣기
    heapq.heapify(files)

    total_cost = 0  # 총 비용 누적

    # 파일이 하나만 남을 때까지 반복
    while len(files) > 1:
        # 가장 작은 두 개의 파일을 선택
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        # 두 파일을 합친 비용 계산
        merge_cost = first + second
        total_cost += merge_cost  # 비용 누적

        # 합친 파일을 다시 힙에 넣음
        heapq.heappush(files, merge_cost)

    return total_cost


# 입력 처리
def main():
    # 테스트 케이스 개수
    T = int(sys.stdin.readline().strip())

    results = []
    for _ in range(T):
        # 파일 개수 입력
        K = int(sys.stdin.readline().strip())

        # 파일 크기 리스트 입력
        files = list(map(int, sys.stdin.readline().strip().split()))

        # 최소 비용 계산
        results.append(str(min_merge_cost(K, files)))

    # 결과 출력
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
