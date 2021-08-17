n=int(input())
pl=sum(list(map(int,input().split())))
m=int(input())
ml=sorted(list(map(int,input().split())))[::-1] 
for i in range(m):
    drain=100-ml[i]
    if pl<drain:
        break
    ml[i]+=drain
    pl-=drain
print(ml.count(100))