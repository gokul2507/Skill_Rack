a,b,c=[int(input()) for i in range(3)]
if a==b and b==c:print("equilateral")
elif a==b or b==c or c==a: print("isosceles")
else:print("scalene")
