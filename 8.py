a=float(input())
b=float(input())
c=input()

if b==0.0 and (c=="/" or c=="mod" or c=="div"):
    print("Деление на 0!")
elif c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="div":
    print(a//b)
elif c=="mod":
    print(a%b)
else:
    print(a**b)