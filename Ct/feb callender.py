def dates(q):
    if (q%4==0 and q%100) or q%400==0:
        return 30
    return 29
a,b=input().split()
day="SUN MON TUE WED THU FRI SAT".split()
a=int(a)
b=(day.index(b)+3)%7
d=b
print("S M T W T F S")
print("* "*d,end='')
date=dates(a)
for i in range(1,date):
    d+=1
    if d==8:
        print()
        d=1
    print(i,end=' ')
print("* "*(7-d))
