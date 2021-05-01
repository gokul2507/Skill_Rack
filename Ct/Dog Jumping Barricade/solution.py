for i in range(int(input())):
    x,y,z=[int(n) for n in input().split()]
    a=[int(n) for n in input().split()]
    c=0 
    for i in range(z):
        k=1
        d=x 
        while d<a[i]:
            d=(d-y)+x 
            k+=1 
        c+=k 
    print(c)
