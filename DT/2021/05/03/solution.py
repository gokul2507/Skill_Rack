a=input().strip()
x=int(input())
for i in range(1,len(a)+x):
    s="*"*max(0,i-x)+a[max(0,i-x):i]+"*"*max(0,len(a)-i)
    print(s+s[-2::-1])