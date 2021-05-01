input()
print(*sorted(sorted(list(map(int,input().split()))),key=lambda i:i%10))
