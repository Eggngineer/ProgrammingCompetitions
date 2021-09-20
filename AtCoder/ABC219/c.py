from ABC219.b import T


def dic_check(s,t,j):
    if X.index(s[j]) < X.index(t[j]):
        return s,t
    else:
        return t,s

def if_max(s,t):
    if len(s) < len(t):
        return s,t
    else:
        return t,s

def dic(s , t):
    L = min(len(s), len(t))
    if not len(s) == len(t):
        for i in range(L):
            if not s[i] == t[i]:
                s,t = dic_check(s,t,i)
                break
            if i == L-1:
                s,t = if_max(s,t)
    return s,t

def select_sort(S):
    for i ,e in enumerate(S):
        break


X_tmp = input()
X=[]
for i in range(len(X_tmp)):
    X.append(X_tmp[i])

N = int(input())

S = []
for i in range(N):
    a=input()
    S.append(a)
