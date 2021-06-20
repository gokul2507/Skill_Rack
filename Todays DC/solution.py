s=list(map(str,input().split()));a=0
while(True):
    try:t=input().strip();s.append(t);a=1
    except:break
if a==1:print(*s[::-1])
else:
    for i in s[::-1]:print(i)
print(len(s))