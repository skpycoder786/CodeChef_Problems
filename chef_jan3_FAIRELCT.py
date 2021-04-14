try:                    # for handling EOF error in online IDEs.
    T=int(input())
    LResult=list()

    def sumoflist(lst):
        add=0
        for i in range(len(lst)):
            add=add+lst[i]
        return add

    for i in range(T):
        N,M=input().split()
        N,M=int(N),int(M)
        Maxswap=min(N,M)
        
        NA=input().split()
        for j in range(N):
            NA[j]=int(NA[j])
        NA.sort()
        #check1) print(NA)
            
        MB=input().split()
        for j in range(M):
            MB[j]=int(MB[j])
        MB.sort()
        MB.reverse()
        #check2) print(MB)
        
        if(sumoflist(NA) > sumoflist(MB)):      # vote of john > vote of jack
            LResult.append(0)
        else:
            count=0
            for j in range(Maxswap):
                NA[j],MB[j]=MB[j],NA[j]
                count=count+1
                #check3) print(NA,MB)
                if(sumoflist(NA) > sumoflist(MB)):
                    LResult.append(count)
                    break
                else:
                    if j<(Maxswap-1):
                        continue
                    else:
                        LResult.append(-1)
                    
    for i in range(T):
        print(LResult[i])

except:
    pass