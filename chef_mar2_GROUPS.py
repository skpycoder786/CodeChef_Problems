def no_group(st):
    group=0
    if st[0]=='1' :
        group+=1
    for i in range(1,len(st)):
        if st[i] == '1' :
            if st[i-1]=='0' :
                group+=1
            else:
                continue
        else:
            continue
    return group        

# Driver Code.....
T=int(input())
LResult=list()
for i in range(T):
    row_str=input()
    ans=no_group(row_str)
    LResult.append(ans)        
for i in range(T):
    print(LResult[i])          