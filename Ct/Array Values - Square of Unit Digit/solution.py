input()
print(*[(i%10)*(i%10) for i in list(map(int,input().split()))])
