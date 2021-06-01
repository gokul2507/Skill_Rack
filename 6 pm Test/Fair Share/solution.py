s,x=map(int,input().split())
l=list(map(int,input().split()))
f=float(input())
t=sum(l)-l[x-1]
print("%0.1f"%abs(t/2-f)) if t//2!=f else print("FAIR SHARE")