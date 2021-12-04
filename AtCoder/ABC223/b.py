import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

alpha2num = lambda c: ord(c) - ord('a') + 1
num2alpha = lambda c: chr(c+64)

X = S()
xmin=0
xmax=1e10000
xminSTR=""
xmaxSTR=""

def alph210(X):
    y = 0
    for i in range(len(X)):
        y+=alpha2num(X[i])
        if i != len(X)-1:
            y*=10
    return y

def slide(a):
    tmp = a.pop(0)
    a.append(tmp)

for _ in range(len(X)):
    tmp = alph210(X)
    if xmin >= tmp:
        xminSTR = X
    if xmax <= tmp:
        xmaxSTR = X
    slide(X)

print(xminSTR)
print(xmaxSTR)
