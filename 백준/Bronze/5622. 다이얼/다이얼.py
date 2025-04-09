dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())		# 알파벳 단어 입력
result = 0

for i in alpha:
    for j in dial:
        if i in str(j):		# str(j) = 'A', 'B', 'C', •••
            num = dial.index(j) + 3		# 각 알파벳 별 필요한 시간
            result += num
print(result)