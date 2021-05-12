l=[]
for i in range(int(input())):
    a,x,y,z=input().split()
    x,y,z=int(x),int(y),int(z)
    if x+y+z>=150:
        l.append(a)
print(*sorted(l),sep='\n')
