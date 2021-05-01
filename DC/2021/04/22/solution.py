a=int(input())
z=input().strip().split()
t=1
'''a=2
z=['0','1']'''
c=0
f=0
while t:
    t=0
    p=z[::]
    for i in range(a):
        if z[i]=='2':
            if i and z[i-1]=='1':
                p[i-1]='2'
                f=1
                if i-1 and z[i-2]=='1':
                    t=1
            if i<a-1 and z[i+1]=='1':
                p[i+1]='2'
                f=1
                if i+1<a-1 and z[i+2]=='1':
                    t=1
    c+=1
    z=p
print(c+f,z.count('1'))
