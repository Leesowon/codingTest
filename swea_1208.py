import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11) :
    dump = int(input())
    box_height = list(map(int, input().split()))

    for _ in range(dump) :
        maxh = max(box_height)
        minh = min(box_height)

        max_idx = box_height.index(maxh)
        min_idx = box_height.index(minh)

        if (maxh-minh) <= 1 :
            break

        box_height[max_idx] -= 1
        box_height[min_idx] += 1

    final_maxh = max(box_height)
    final_minh = min(box_height)

    final_max_idx = box_height.index(final_maxh)
    final_min_idx = box_height.index(final_minh)

    print(f"#{tc} {final_maxh-final_minh}")