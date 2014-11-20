g=int(input())
if g-(int(g//100))*100 in range(11,15):
    print(g, "программистов")
elif g-(int(g//10))*10 in range(2,5):
    print(g, "программиста")
elif g-(int(g//10))*10==1:
    print(g, "программист")
else:
    print(g, "программистов")