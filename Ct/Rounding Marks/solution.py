for _ in range(int(input())):
    x=int(input())
    t=x%5
    if x<38 or t==0:
        t=0
    elif t>2:
        x+=5-t
    print(x)
