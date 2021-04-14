# Method-1) 
# only for understanding, but for use we will pick 2nd method.

# Main Logic Fn.....
#def tripletValue(x,y,z):
#    a=abs(x-y)
#    b=abs(y-z)
#    c=abs(z-x)
#    return (a+b+c)
# Driver Code.....
#T=int(input())
#LResult=list()
#for i in range(T):
#    maxStore=[]
#    N=int(input())
#    lst=list(map(int,input().split()))
#    for j in range(N-2):
#        x=lst[j]
#        y=lst[j+1]
#        z=lst[j+2]
#        temp=tripletValue(x,y,z)
#        maxStore.append(temp)
#    ans=max(maxStore)    
#    LResult.append(ans)
#for i in range(T):
#    print(LResult[i])

# Method-2)
# But Above logic will take a lot of time when N's values become higher.
# That's why we will use another logic as below, which is more important then previous logic.

try:
    T=int(input())
    LResult=list()
    for i in range(T):
        N=int(input())
        lst=list(map(int,input().split()))
        ans=2*(max(lst)-min(lst))    
        LResult.append(ans)
    for i in range(T):
        print(LResult[i])    # cook your dish here
except:
    pass    