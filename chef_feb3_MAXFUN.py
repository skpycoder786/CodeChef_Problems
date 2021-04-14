# Main logic Fn.....   
def timeSlot(P,LR):
    P_hr,P_min,P_mode = int(P[:2]),int(P[3:5]),P[6:]
    if P_hr == 12 :
        P_hr=00
    #check-1) print(P_hr,P_min,P_mode)
     
    L=LR[:8]
    L_hr,L_min,L_mode = int(L[:2]),int(L[3:5]),L[6:]
    if L_hr == 12 :
        L_hr=00
    R=LR[9:]
    R_hr,R_min,R_mode = int(R[:2]),int(R[3:5]),R[6:]
    if R_hr == 12 :
        R_hr=00
    #check-2) print(L,"*",R)
    
    # CASE-1 :
    if P_mode == 'AM' :
    
        # TYPE : AM-AM
        if L_mode == 'AM' and R_mode == 'AM' :
            # for Ldig
            if P_hr >= L_hr :
                if P_hr > L_hr :
                    Ldig=1
                elif P_hr==L_hr :
                    if P_min >= L_min :
                        Ldig=1
                    else:
                        Ldig=0
            else:
                Ldig=0                
            # for Rdig
            if P_hr <= R_hr :
                if P_hr < R_hr :
                    Rdig=1
                elif P_hr==R_hr :
                    if P_min <= R_min:
                        Rdig=1
                    else:
                        Rdig=0
            else:
                Rdig=0
            # and of both
            return str( Ldig and Rdig )
        
        # TYPE : AM-PM    
        elif L_mode == 'AM' and R_mode == 'PM' :
            if P_hr >= L_hr :
                if P_hr > L_hr :
                    return '1'
                elif P_hr==L_hr :
                    if P_min >= L_min :
                        return '1'
                    else:
                        return '0'
            else:
                return '0'
        
        # TYPE : PM-AM        
        elif L_mode == 'PM' and R_mode == 'AM' :
            if P_hr <= R_hr :
                if P_hr < R_hr :
                    return '1'
                elif P_hr==R_hr :
                    if P_min <= R_min:
                        return '1'
                    else:
                        return '0'
            else:
                return '0'
        
        # TYPE : PM-PM            
        elif L_mode == 'PM' and R_mode == 'PM' :
            return '0'

    # CASE-2 :
    if P_mode == 'PM' :
        
        # TYPE : AM-AM
        if L_mode == 'AM' and R_mode == 'AM' :
            return '0'
        
        # TYPE : AM-PM    
        elif L_mode == 'AM' and R_mode == 'PM' :
            if P_hr <= R_hr :
                if P_hr < R_hr :
                    return '1'
                elif P_hr==R_hr :
                    if P_min <= R_min:
                        return '1'
                    else:
                        return '0'
            else:
                return '0'
        
        # TYPE : PM-AM        
        elif L_mode == 'PM' and R_mode == 'AM' :
            if P_hr >= L_hr :
                if P_hr > L_hr :
                    return '1'
                elif P_hr==L_hr :
                    if P_min >= L_min :
                        return '1'
                    else:
                        return '0'
            else:
                return '0'
        
        # TYPE : PM-PM            
        elif L_mode == 'PM' and R_mode == 'PM' :
            # for Ldig
            if P_hr >= L_hr :
                if P_hr > L_hr :
                    Ldig=1
                elif P_hr==L_hr :
                    if P_min >= L_min :
                        Ldig=1
                    else:
                        Ldig=0
            else:
                Ldig=0                
            # for Rdig
            if P_hr <= R_hr :
                if P_hr < R_hr :
                    Rdig=1
                elif P_hr==R_hr :
                    if P_min <= R_min:
                        Rdig=1
                    else:
                        Rdig=0
            else:
                Rdig=0
            # and of both
            return str( Ldig and Rdig )
    
# Driver Code.....
T=int(input())
LResult=list()
for j in range(T):
    Pstr=input()   # meet time
    N=int(input())  # numbers of friend
    decision_str=''
    for i in range(N):
        LRstr=input()  # timeslot's string
        digit=timeSlot(Pstr,LRstr)
        decision_str+=digit
    LResult.append(decision_str)

# Results    
for j in range(T):
    print(LResult[j])    

# Here we can use try-except for resolving run-time-error by 'pass-the-error' through except.    