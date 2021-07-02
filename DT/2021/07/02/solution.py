z=[list(map(int,input().split())) for _ in range(int(input()))]
x=int(input())
print(sum([1 if i<=x<j else 0 for i,j in z]))