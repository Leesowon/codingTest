import sys
input = sys.stdin.readline

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dis = []

for i in range(1, n) :
    distance = sensor[i] - sensor[i-1]
    if distance == 0 :
        continue
    dis.append(distance)

dis.sort(reverse=True)
print(sum(dis[k-1:]))