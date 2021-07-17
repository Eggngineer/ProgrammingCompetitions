import pprint
import numpy as np
H,W,C=(int(x) for x in input().split())
A=[]
ranked=[]
for i in range(H):
    A.append(list(int(x) for x in input().split()))
# print("====================")
# pprint.pprint(A,width=20)
A=np.asarray(A)
