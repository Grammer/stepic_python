string=input().lower()
#summ=0
#for i in string:
#    if i=="g" or i=="c":
#        summ+=1
c=string.count('c')
g=string.count('g')
print(((c+g)*100)/len(string))
