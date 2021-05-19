input()
l=sorted(list(map(int,input().split())),key=lambda i:(i/10)%10)
l=sorted(l,key=lambda i:i%10)
print(*l)