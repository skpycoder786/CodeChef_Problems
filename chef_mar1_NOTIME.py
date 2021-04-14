N,H,x=input().split()
N,H,x=int(N),int(H),int(x)
lst=list(map(int,input().split()))
rest=H-x
app_lst=[]
for i in range(N):
    if lst[i] >= rest :
        app_lst.append(lst[i])
if len(app_lst) > 0 :
    print("YES")
else:
    print("NO")