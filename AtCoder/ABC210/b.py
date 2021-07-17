T="Takahashi"
A="Aoki"
N=int(input())
S_p=input().split()
S=[]
for x in S_p[0]:
    S.append(x)

St=S[0::2]
Sa=S[1::2]

if '1' in St and '1' in Sa:
    if St.index('1')<=Sa.index('1'):
        print(T)
    else:
        print(A)
elif '1' in St:
    print(T)
else:
    print(A)
