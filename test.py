

def find(num) :
    if parent[num] == num :
        return num
    return parent[num] = find(parent[num])

parent = [i for i in range(n+1)]
