import sys
input = sys.stdin.readline

def sort_gpt(numbers) :
    def gpt_key(num) :
        if '.' in num :
            x, y = num.split('.')
            return (int(x), int(y)) # 정수부와 소수부 나눠 비교
        else :
            return (int(num), -1) # 소수점이 없는 경우 소수부를 -1로 설정

    numbers.sort(key=gpt_key) # key : 정렬 기준
    # 각 요소에 gpt_key를 적용
    # 반환된 키를 기준으로 정렬

n = int(input())
numbers = [input().strip() for _ in range(n)]
sort_gpt(numbers)

for num in numbers :
    print(num)