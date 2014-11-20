z=input()
if z == "треугольник":
    a=float(input())
    b=float(input())
    c=float(input())
    p=(a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**(0.5))
elif z=="прямоугольник":
    a=float(input())
    b=float(input())
    print(a*b)
else:
    a=float(input())
    print(3.14*a**2)