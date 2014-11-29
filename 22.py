a = sorted([int(i) for i in input().split()])
b = []
for i in range(0, len(a)-1):
    if a.count(a[i]) > 1 :
        if b.count(a[i]) == 0:
            b.append(a[i])
for i in range(0, len(b)):
    print(b[i], end=" ")