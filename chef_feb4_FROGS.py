# Main Logic Fn.....
def update_temp_W(W_and_posi):
    t=list(W_and_posi.items())  # list of (W,posi) tuples
    t.sort(key = lambda x: x[0])    # sort on bases of W
    t.reverse()
    t.sort(key = lambda x: x[1])    # sort on bases of posi
    #check-6) print(t)
    updated_lst=[]
    for tup in t:
        updated_lst.append(tup[0])
    return updated_lst
# Testing of function :     
#d={45:3 ,20:2, 40:3, 30:3, 10:1}
#ans=update_temp_W(d)    
#print(ans) 
            
# Driver Code.....
T=int(input())
LResult=list()

for i in range(T):
    N=int(input())
    W=list(map(int,input().split()))
    L=list(map(int,input().split()))
    #check-1) print(type(W[2]))
    #check-2) print(L)
        #Extra
        #W_and_L=dict()
        #W_and_posi=dict()
        #for i in range(N):
        #    W_and_L[W[i]]=L[i]
        #    W_and_posi[W[i]]=i
        # follow short method for making dictionaries as below.....
    W_and_L=dict(zip(W,L))
    W_and_posi=dict(zip(W,list(x for x in range(N))))
    back=0
    sorted_W=sorted(W)
    #check-3) print(sorted_W) 
    temp_W=W[:]
    while True :
        if temp_W == sorted_W :
            break
        for i in range(N-1):
            if temp_W[i] > temp_W[i+1] :
                back+=1
                W_and_posi[temp_W[i]] += W_and_L[temp_W[i]]
            else:
                continue
        #check-4) print(W_and_posi)        
        temp_W.clear()
        temp_W=list(update_temp_W(W_and_posi))
        #check-5) print(temp_W)
    LResult.append(back)
        
for i in range(T):
    print(LResult[i])          