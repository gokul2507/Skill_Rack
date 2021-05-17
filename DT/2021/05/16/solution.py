n=int(input())
c=1 
s='abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    for j in range(n):
        if i%2==n%2:
            print(s[(c-1)%26],end=" ")
        else:
            print(c,end=" ")
        c+=1 
    print() 