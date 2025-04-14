name = input().strip()

for i in range(len(name)//2) :
    if name[i] != name[len(name)-1-i] :
        print(0)
        exit(0)

print(1)