m=0
for i in range(2,int(input())+2):
    s=i
    for j in range(i):
        print(("-"*m)+("* "*s))
        m+=1
        s-=1