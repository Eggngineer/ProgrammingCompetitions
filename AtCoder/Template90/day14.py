N = int(input())
A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))
A.sort()
B.sort()
ans = 0
for i in range(N):
    ans += abs(A[i]-B[i])
print(ans)
