lst = [int(i) for i in input().split()]
x = int(input())
if x not in lst:
    print("Отсутствует")
else:
    for i in lst:
        if x == lst[i]:
            print(i, end=" ")