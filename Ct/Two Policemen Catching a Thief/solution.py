for i in range(int(input())):
    x=list(map(int,input().split()))
    p1,p2=abs(x[0]-x[2]),abs(x[1]-x[2])
    if p1<p2:print("Police1")
    elif p2<p1:print("Police2")
    else:print("Both")
