def isOK(M) ->bool:
    cutPoint,cutCount=0,0
    for i in range(N):
        if A[i] - cutPoint >= M and L - A[i] >= M:
            cutPoint = A[i]
            cutCount += 1

    if cutCount>=K:
        return True
    else:
        return False

def binary_search_generalized() -> int:
    left, right = -1, L+1

    while(right - left > 1):
        mid = int(left + (right - left) / 2)

        if (not isOK(mid)):
            right = mid
        else:
            left = mid

    return left


N,L = (int(x) for x in input().split())
K = int(input())
A = list(map(int, input().strip().split()))

print(binary_search_generalized())
