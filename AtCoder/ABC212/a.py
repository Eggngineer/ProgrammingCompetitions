A,B=(int(x) for x in input().split())
word=""
if A*B>0:
    word+="Alloy"
elif B==0:
    word+="Gold"
elif A==0:
    word+="Silver"
print(word)
