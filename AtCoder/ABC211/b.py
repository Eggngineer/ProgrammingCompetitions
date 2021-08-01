S=[]
for i in range(4):
    S.append(str(input()))
if len(list(set(S)))==4:
    print("Yes")
else:
    print("No")

