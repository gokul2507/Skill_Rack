for i in range(int(input())):
    n,c,f=map(int,input().split())
    if n-f+1>=c:
        print(f+c-1)
    else:
        c=(c-(n-f+1))%n
        if c==0:
            c=n
        print(c)
