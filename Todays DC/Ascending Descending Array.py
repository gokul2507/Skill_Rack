m=int(input())
ml=list(map(int,input().split()))
n=int(input())
nl=list(map(int,input().split()))
if len(set(ml))==1 and len(set(nl))==1:
    if nl[0]<ml[0]:
        print(*nl)
        print(*ml)
    else:
        print(*ml)
        print(*nl)
elif sorted(ml)[::-1]==ml and len(set(nl))==1:
    print(*nl)
    print(*ml)
elif sorted(nl)[::-1]==nl and len(set(ml))==1:
    print(*ml)
    print(*nl)
elif len(set(ml))==1:
    print(*nl)
    print(*ml)
elif sorted(ml)==ml:
    print(*ml)
    print(*nl)
else:
    print(*nl)
    print(*ml)