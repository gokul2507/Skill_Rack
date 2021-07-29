import re
alp=lambda x:("".join(re.findall("[a-zA-Z]",x)),int("".join(re.findall("[0-9]",x))))
input()
for i in sorted(map(alp,input().split())):
    print(i[1],end=' ')