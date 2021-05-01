n,l=int(input()),list(map(int,input().split()))
print(sum([i for i in l if i%2])-sum([i for i in l if i%2==0]))
