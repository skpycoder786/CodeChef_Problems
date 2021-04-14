T=int(input())
LResult=list()

for i in range(T):
    l=list(map(float,input().split()))
    dis=1
    for i in l:
        dis=dis*i
    tt=float(100/dis)
    ftt=round(tt,2)
    if(ftt<9.58):
        LResult.append("YES")
    else:
        LResult.append("NO")
        
for i in range(T):
    print(LResult[i])
    
