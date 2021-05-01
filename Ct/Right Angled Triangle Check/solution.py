a,b,c=[int(input()) for i in range(3)]
a,b,c=a*a,b*b,c*c
if a+b==c or a+c==b or b+c==a:print("YES")
else:print("NO")
