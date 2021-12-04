
def bitOPS(N=0):
    ans = []

    for i in range(1<<N):
        base=""
        judge = 0
        for j in reversed(range(N)):
            if i & (1 << j)==0:
                base += '('
                judge += 1
            else:
                base += ')'
                judge += -1
            if judge<0:
                break
        if judge==0:
            ans.append(base)


    ans.sort()

    return ans


N = int(input())
an=bitOPS(N)
for x in an:
    print(x)
