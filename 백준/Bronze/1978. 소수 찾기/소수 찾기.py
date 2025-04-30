n = int(input())
numbers = list(map(int, input().split()))

# def prime(nn) :
#     for i in range(2, nn) :
#         if nn % i == 0 :
#             return False
#     return True

# ans = 0
for num in numbers :
    if num == 1 :
        n -= 1
        
    for v in range(2, num) :
        if num % v == 0 :
            n -= 1
            break

    # if prime(num) :
    #     ans += 1
print(n)