import re 
s=input().strip()
alp=re.findall("[a-zA-Z]",s) 
t=''
for i in s:
    if i.isdigit():
        t+=i 
    else:
        print(''.join(alp)*int(t)) 
        t=''
        alp.pop(0)