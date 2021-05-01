x=int(input().split()[1])
print(sum(sorted(map(int,input().split()))[-x:]))
