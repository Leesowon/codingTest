import sys
input = sys.stdin.readline

n = int(input())
cnt = n

for _ in range(n) :
    word = input().strip()
    for i in range(len(word)-1) :
        # 같은 단어가 연달아 있있다면 Continue
        if word[i] == word[i+1] :
            continue
        # 같은 단어가 연속해서 나타나지 않는다면
        if word[i] in word[i+1:] :
            cnt -= 1
            break
            
print(cnt)