try:
    n=int(input())
    lst=[]
    for i in range(1,11):
        if n%i == 0 :
            lst.append(i)
        else:
            pass
    print(max(lst))        
except:
    pass