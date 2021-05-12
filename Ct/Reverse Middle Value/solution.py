n=int(input())
for i in range(n):
    s=input().strip()
    print(s[0],s[1:-1][::-1],s[-1],sep='')
