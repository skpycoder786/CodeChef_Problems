T=int(input())
finalList=[]    #for storing combined character's string

def BinaryToDecimal(binary):  #function for convertig binary code to decimal
    decimal, i = 0, 0
    while(binary != 0):  
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)  
        binary = binary//10
        i += 1
    return (decimal)
    
def listToString(s):  
    str1 = ""       # initialize an empty string       
    for ele in s:   # traverse in the string  
        str1 += ele     
    return str1        
    
for i in range(T):
    N=int(input()) #size of binary string to decode
    binStr=input()
    n=int(N/4)
    LResult=[]  # for storing single character
    for j in range(n):
        str=""
        str=binStr[4*j : 4*j+4]
        binary=int(str)
        intvalue=BinaryToDecimal(binary)
        intvalue=97+intvalue
        chrvalue=chr(intvalue)
        LResult.append(chrvalue)
        #check1) print(chrvalue)        
    StrResult=listToString(LResult)
    finalList.append(StrResult)
    
for i in range(T):
    print(finalList[i])
