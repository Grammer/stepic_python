a = int(input())
b = int(input())
s = 0
z = 0
if a % 3 == 1:
    a += 2
elif a % 3 == 2:
    a += 1
for i in range(a, b+1, 3):
    s += i
    z+=1
print(s/z)