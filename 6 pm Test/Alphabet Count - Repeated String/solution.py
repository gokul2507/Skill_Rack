a=input().strip()
b=int(input())
c=input().strip()
x=b//len(a)+1 
a=a*x 
print(a[:b].count(c))