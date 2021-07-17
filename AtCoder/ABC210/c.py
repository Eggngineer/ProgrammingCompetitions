N,K=(int(x) for x in input().split())
c=list(int(x) for x in input().split())
maxlen=0
a = []

for i in range(N-K+1):
    Hatena=c[i:K+i:1]
    Hatena=len(list(set(Hatena)))
    a.append(Hatena)

print(max(a))



##TLE...
