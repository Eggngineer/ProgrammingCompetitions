N,A,X,Y=(int(x) for x in input().split())

output=0
if N<=A:
    print(N*X)
else:
    print(A*X+(N-A)*Y)
