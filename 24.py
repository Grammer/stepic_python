n=int(input())
a=[]
for i in range(0,n):
    i+=1
    for j in range(0,i):
        a.append(i)
print(*a[:n], sep=" ")