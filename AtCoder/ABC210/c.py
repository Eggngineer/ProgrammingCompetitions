N,K=(int(x) for x in input().split())
c=list(int(x) for x in input().split())
Hatena=c[0:K+0:1]
MaxLen = 1

for i in range(N-K):
    Hatena.pop(0)
    Hatena.append(c[K+i])
    if MaxLen<len(list(set(Hatena))):
        MaxLen=len(list(set(Hatena)))

print(MaxLen)





