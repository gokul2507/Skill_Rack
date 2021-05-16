s=input().strip()
cb=list("""abcdefghijklmnopqrstuvwxyz., ?'" """)[:-1]
for i in range(0,len(s),5):
    x=''
    for j in s[i:i+5]:
        if j.islower():x+='0'
        else:x+='1'
    a=int(x,2)
    print(cb[a],end='')
