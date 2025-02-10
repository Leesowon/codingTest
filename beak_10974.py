N=int(input())

def permutation(n,r,temp=[]):
    if r==0:
        return print(*temp)
    else:
        for i in range(1,n+1):
            if i not in temp:
                temp.append(i)
                permutation(n,r-1,temp)
                temp.remove(i)

permutation(N,N)