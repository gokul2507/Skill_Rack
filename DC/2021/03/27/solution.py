d={}
def qw(w,e):
    if w!=1:
        e+='s'
    return str(w)+" "+e+" "
for _ in range(int(input())):
    s=input().strip().split("\\")
    t=d.get(s[1],[set(),set()])
    i=0
    if len(s)-2==1:
        i=1
    t[i].add(s[2])
    d[s[1]]=t
for i in sorted(d):
    print(i+" - "+qw(len(d[i][0]),"folder")+qw(len(d[i][1]),"file"))
