def check(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 1 
    return 0 
for _ in range(int(input())):
    if check(int(input())):
        print("yes")
    else:
        print("no")
