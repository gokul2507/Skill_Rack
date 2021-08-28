al="abcdefghijklmnopqrstuvwxyz"
nl="0123456789"
op=""
a=input().strip()
# a='cHesS8880007'
for i in a:
    if i.lower() not in op:
        print(i,end='')
        op+=i.lower()
        al=al.replace(i.lower(),'')
        nl=nl.replace(i.lower(),'')
    else:
        if i.isdigit():
            i=int(i)
            for j in nl:
                j=int(j)
                if i<j:
                    break
            else:
                j=nl[0]
            j=str(j)
            nl=nl.replace(j,'')
            op+=j
            print(end=j)
        else:
            for j in al:
                if ord(j)>ord(i.lower()):
                    break
            else:
                j=al[0]
            al=al.replace(j,'')
            op+=j
            if i.isupper():
                j=j.upper()
            print(end=j)
    # print(op)