s=input().strip();l=len(s);st=((l+1)//2)-1;et=((l+1)//2)-1
for i in range((l+1)//2):  
    for j in range(l):  
        if(i==j):        
            print(s[i],end="")     
        elif(l-1-i==j):    
            print(s[l-1-i],end="")    
        elif(j==st):        
            print(s[st],end="")    
        elif(j==et):        
            print(s[et],end="")     
        else:           
            print("*",end="")   
    st-=1  
    et+=1   
    print()