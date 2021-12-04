#normally one integer
a = int(input())

#integers more than one
a,b = list(map(int, input().strip().split()))

#integers more than one as list
A = list(map(int, input().strip().split()))

#integers as matrix
"""
N
s1 t1 u1
s2 t2 u2
s3 t3 u3
...
sn tn un
"""
N = int(input().strip())
grid = []
for i in range(N):
    array = list(map(int, input().strip().split()))
    grid.append(array)


#faster input
# import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
N = I()
A = [LI() for _ in range(N)]

