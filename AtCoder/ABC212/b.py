out = ["Weak","Strong"]
flag = 1
X=[]
ipt=str(input())
for x in ipt:
    X.append(int(x))
if len(list(set(X)))==1:
    flag = 0
for i in range(3):
    if X[i+1]%10!=(X[i]+1)%10:
        break
    if i==2:
        flag = 0

print(out[flag])


