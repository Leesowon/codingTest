import sys
input = sys.stdin.readline

def make_set(n) :
    parent = [i for i in range(n+1)]
    rank = [1] * (n+1)
    return parent, rank

def find(parent, x) :
    if parent[x] != x : # 루트가 아니면
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b) :
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rank[rootA] > rank[rootB] :
        parent[rootB] = rootA
    elif rank[rootB] > rank[rootA] :
        parent[rootA] = rootB
    else :
        parent[rootB] = rootA
        rank[rootA] += 1

n, m = map(int, input().split()) # n : 노드의 갯수

parent, rank = make_set(n)

for _ in range(m) :
    num, a, b = map(int, input().split())
    if num == 0 :
        union(parent, rank, a, b)
    elif num == 1 :
        if find(parent, a) == find(parent, b) :
            print("YES")
        else :
            print("NO")