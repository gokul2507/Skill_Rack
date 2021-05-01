s=input().strip()
c=[i for i in s if i.lower() in 'aeiou'][::-1]
for i in s:
    print(c.pop(0),end='') if i.lower() in 'aeiou' else print(i,end='')
