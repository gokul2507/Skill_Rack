d={1:"@_",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
l=[]
for i in input().strip():
    l.append(d[int(i)])
t=-len(l)
def find(t,s):
    if t>=0:
        print(s,end=' ')
        return
    for i in l[t]:
        find(t+1,s+i)
find(t,"")
