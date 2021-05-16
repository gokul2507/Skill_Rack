l=[]
for  i in range(int(input())):
    l.append(input().split())
x=input().strip()
for i in l:
    if i[1]==x:
        print(i[0])
