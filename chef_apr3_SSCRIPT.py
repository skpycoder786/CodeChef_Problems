import re
T=int(input())
LResult=list()

for i in range(T):
    N,K=input().split()
    N,K=int(N),int(K)
    giv=input()
    s=''
    for i in range(K):
        s+='\*'
    x = re.findall(s,giv)    
    if len(x) > 0 :
        ans='YES'
    else:
        ans='NO'
    LResult.append(ans)
        
for i in range(T):
    print(LResult[i])
    
