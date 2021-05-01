for a in range(int(input())):
    n=int(input())
    z=list(map(int,input().split()))
    y=[i for i in z if i%2]
    x=[i for i in z if i%2==0]
    print(sum(x))
    print(sum(y))
