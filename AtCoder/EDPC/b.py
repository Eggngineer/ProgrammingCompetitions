import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

N , K = LI()
h = LI()

dp = [0] * N
for i in range(1,N):
    dp[i]=abs(h[i]-h[i-1])+dp[i-1]
    for j in range(1,K+1):
        if i-j>=0:
            dp[i]=min(dp[i-j]+abs(h[i]-h[i-j]),dp[i])

print(dp[N-1])
