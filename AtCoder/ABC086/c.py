import numpy as np
def solve(stt,ent,fromCo,toCo):
    x,y=0,1
    time=ent-stt
    dis =(np.asarray(toCo)-np.asarray(fromCo)).sum()
    return dis<=time and time%2 == dis%2


schedule=[0]
co=[[0,0]]
blist=[]
N = int(input())
for i in range(N):
    data = list(int(x) for x in input().split())
    schedule.append(data[0])
    co.append([data[1],data[2]])

for i in range(1,N+1):
    blist.append(solve(schedule[i-1],schedule[i],co[i-1],co[i]))
print(blist)
if np.asarray(blist).all():
    print("Yes")
else:
    print("No")



