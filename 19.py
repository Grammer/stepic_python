string = input()
i=0
if len(string)==1:
    print(string,end="")
    print("1")
else:
    j=1
    while i <= len(string)-1:
        while j <= len(string)-1:
            if string[i] != string[j]:
                print(string[i],end="")
                print(j-i,end="")
                i=j
                if j + 1 > len(string)-1:
                    break
                else:
                    j+=1
            else:
                if j==len(string)-1:
                    print(string[i],end="")
                    print(j-i+1,end="")
                    i=j+2
                    j=i
                else:
                    j+=1