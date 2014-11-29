summ = 0
num = 0
while True:
    a = int(input())
    summ += a
    num += a*a
    if summ == 0:
        break
print(num)