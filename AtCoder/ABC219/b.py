S1 = input()
S2 = input()
S3 = input()
S={1:S1,2:S2,3:S3}
T_tmp = input()
T=[]
for i in range(len(T_tmp)):
    T.append(int(T_tmp[i]))
ans = ""
for i in range(len(T)):
    ans += S[T[i]]

print(ans)
