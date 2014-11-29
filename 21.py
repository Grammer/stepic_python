a = [i for i in input().split()]
if len(a) == 1:
    print(int(a[0]))
else:
    print(int(a[len(a)-1]) + int(a[1]), end = " ")
    for i in range(1, len(a)-1):
        print(int(a[i-1])+int(a[i+1]), end = " ")
    print(int(a[len(a)-2]) + int(a[0]))