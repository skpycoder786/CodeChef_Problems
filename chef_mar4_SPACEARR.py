# Main Logic.....
def winLose(n,a_lst):
    a_lst.sort()
    #check-1) print(a_lst)
    p_lst=[]
    for i in range(n):
        p_lst.append(i+1)
    chance=0
    for i in range(n):
        if a_lst[i] > p_lst[i] :
            return 'Second'
    for i in range(n):
        if a_lst[i] < p_lst[i]:
            chance+=(p_lst[i]-a_lst[i])
        elif a_lst == p_lst :
            continue
    if chance%2==0:
        return 'Second'
    else:
        return 'First'
    
# Driver Code.....
T=int(input())
LResult=list()
for i in range(T):
    N=int(input())
    N_lst=list(map(int,input().split()))
    ans=winLose(N,N_lst)
    LResult.append(ans)        
for i in range(T):
    print(LResult[i])

