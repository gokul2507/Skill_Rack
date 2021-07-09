a,b=input().strip(),input().strip()
for i in range(0,len(b)):
    print(a[:i+1]*int(b[i]))