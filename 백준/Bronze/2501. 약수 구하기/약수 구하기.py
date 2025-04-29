number, k = map(int, input().split())

div = []

for num in range(1, number+1) :
    if number % num == 0 :
        div.append(num)

if len(div) < k :
    ans = 0
else :
    ans = div[k-1]

print(ans)