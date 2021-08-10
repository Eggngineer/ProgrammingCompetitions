N=int(input())
A=list(int(x) for x in input().split())
B=sorted(A)
print(A.index(B[N-2])+1)
