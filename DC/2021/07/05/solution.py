n=[]
while True: 
    try:     
        nl=list(map(int,input().split()))     
        n+=nl  
    except:    
        break
print(*sorted(set(n)))