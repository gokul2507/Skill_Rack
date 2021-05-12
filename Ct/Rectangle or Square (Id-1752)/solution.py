n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if x//4==int(y**0.5):
        print("Square")
    else:
        print("Rectangle")
