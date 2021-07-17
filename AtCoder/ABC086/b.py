from math import sqrt
a,b=(int(x) for x in input().split())

c = int(str(a)+str(b))

i=0
while True:
    if i**2 < c:pass
    elif i**2==c:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
    i+=1

