def mybisect(a, th):
    left,right=0,len(a)-1
    while right - left > 1:
        mid = (right + left) // 2
        if a[mid] >= th:
            right = mid
        else:
            left = mid

    return right

N = int(input())
A = list(map(int, input().strip().split()))
Q = int(input())
tmp = 0
B=[]
for i in range(Q):
    tmp = int(input())
    B.append(tmp)

ans=0
A.sort()
for i in range(Q):
    idx = mybisect(A,B[i])
    print(min(abs(A[idx]-B[i]),abs(A[idx-1]-B[i])))

