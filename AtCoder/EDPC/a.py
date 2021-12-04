N = int(input())
h = list(map(int, input().strip().split()))

dp = [0] * N
for i in range(N):
    if i == 0:
        pass
    elif i == 1:
        dp[i]=abs(h[i]-h[i-1])
    else:
        dp[i]=min(abs(h[i]-h[i-1])+dp[i-1],abs(h[i]-h[i-2])+dp[i-2])

print(dp[N-1])
