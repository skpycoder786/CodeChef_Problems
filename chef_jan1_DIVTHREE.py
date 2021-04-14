T=int(input())
LResult=list()

for i in range(T):
    N,K,D=input().split()
    N=int(N)
    K=int(K)
    D=int(D)
    L=list()
    L=input().split()
    for j in range(len(L)):
        L[j]=int(L[j])
    total_prob=0
    for j in range(len(L)):
        total_prob=total_prob+L[j]
    pos_event=int(total_prob/K)
    if pos_event>D:
        LResult.append(D)
    else:
        LResult.append(pos_event)
        
for i in range(T):
    print(LResult[i])
    
