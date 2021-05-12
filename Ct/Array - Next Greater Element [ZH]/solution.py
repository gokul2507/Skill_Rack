a=int(input())
b=list(map(int,input().split()))
for i in range(a):
      for j in range(i+1,a):
           if b[i]<b[j]:
                print(b[j],end=' ')
                break
       else:
              print(-1,end=' ')
