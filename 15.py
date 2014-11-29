boo=True
while boo==True:
    i=int(input())
    if i<=100:
        if i<10:
            continue
        else:
            print(i)
    else:
        break