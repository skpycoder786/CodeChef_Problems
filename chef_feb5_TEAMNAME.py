# Method-1)
# only for understanding, but for use we will pick 2nd method.

# Main Logic Fn.....
#def notFunWords(lst):   # will return list of non funny words.
#    nofun_lst=[]
#    for word in lst:
#        ft=word[0]    # 'ft' mean first letter
#        for rest in lst:
#            if (rest == word) or (rest[0] == ft) or (rest[1:] == word[1:]) :
#                continue
#            else:
#                rest_lst=list(rest)
#                rest_lst[0]=ft
#                nofun_str="".join(rest_lst)
#                if nofun_str not in lst:
#                    if nofun_str not in nofun_lst:
#                        nofun_lst.append(nofun_str)
#    return nofun_lst         
# Extra test cases
#notFunWords(['aba', 'bbb', 'baa', 'aab'])      
#notFunWords(['dtp', 'ctq', 'rts', 'etp'])        

#def teamNames(lst,lst2):  # will return list of team names.
#    teamLst=[]
#    for word in lst:
#        ft=word[0]    # 'ft' mean first letter
#        for rest in lst:
#            if (rest == word) or (rest[0] == ft) or (rest[1:] == word[1:]) :
#                continue
#            else:
#                l1,l2=list(word),list(rest)
#                l1[0],l2[0]=l2[0],l1[0]
#                s1,s2="".join(l1),"".join(l2)
#                if s1 in lst2:
#                    if s2 in lst2:
#                        temp=word+" "+rest
#                        if temp not in teamLst:
#                            teamLst.append(temp)
#    return teamLst         
#test cases continue...
#teamNames(['abb', 'aaa', 'bba', 'bab'],['aba', 'bbb', 'baa', 'aab'])      
#teamNames(['dtq', 'dts', 'ctp', 'cts', 'rtp', 'rtq', 'etq', 'ets'],['dtp', 'ctq', 'rts', 'etp'])

# Driver Code.....
#T=int(input())
#LResult=list()
#for i in range(T):
#    N=int(input())
#    # task-1 : All strings must be in lower case
#    wordLst=input().split()
#    # check-1) print(wordLst)
#    # task-2 : Making of non funny words list
#    nofunList=notFunWords(wordLst)
#    # check-2) print(nofunList)
#    # task-3 : Making of team names list such that when we swap the first letter of both word of a team name, 
#             # then both of new words are present in funny words list or in given list.
#    finalLst=teamNames(nofunList,wordLst)
#    #check-3) print(finalLst)
#    ans=len(finalLst)
#    print(finalLst)
#    LResult.append(ans)   
#for i in range(T):
#    print(LResult[i])


# Method-2)
# But Above logic will take a lot of time when N's values become higher.
# That's why we will use another logic as below, which is more important then previous logic.

try:
    # Main Logic Fn.....
    def teamNames(lst):
        # making of dictionary such as {'rest string as key' : '1st character as value', ... }
        DIC={}
        for word in lst:
            fc=word[:1]
            k=word[1:]
            if k in DIC.keys():
                value=DIC[k]
                value.append(fc)
                continue
            DIC[k]=[fc]
        #check-1) print(DIC)
        # making of unique team_names pairs
        kv_lst=list(DIC.items())
        pair=0
        for i in range(len(kv_lst)-1):
            value_lst=kv_lst[i][1]
            for j in range(i+1,len(kv_lst)):
                value_lst1=kv_lst[j][1]
                if value_lst1 == value_lst :
                    continue
                else:
                    diff_v=[]
                    buf=value_lst[:]
                    for i in value_lst1:
                        if i not in value_lst:
                            diff_v.append(i)
                        else:
                            buf.remove(i)
                            pass
                    #check-2) print(diff_v)        
                    pair += (len(buf)*len(diff_v))
        count_names=(2*pair)
        return count_names
        #check-3) print(count_names)        

    # Driver Code.....
    T=int(input())
    LResult=list()
    for i in range(T):
        N=int(input())
        wordLst=input().split()
        ans=teamNames(wordLst)
        LResult.append(ans)    
    for i in range(T):
        print(LResult[i])
except:
    pass