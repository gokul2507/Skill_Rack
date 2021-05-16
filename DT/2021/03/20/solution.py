def num(s):
    if s=="001"*5:
        return 1
    if s=="111001111100111":
        return 2
    if s=="111001111001111":
        return 3
    if s=="101101111001001":
        return 4
    if s=="111100111001111":
        return 5
    if s=="111100111101111":
        return 6
    if s=="111"+"001"*4:
        return 7
    if s=="111101111101111":
        return 8
    if s=="111101111001111":
        return 9
    return 0
z=[[] for _ in range(4)]
for i in range(5):
    x=input().strip()
    l=0
    for i,j in [[0,3],[4,7],[10,13],[14,17]]:
        z[l].append(x[i:j])
        l+=1
for i in z[:2]:
    print(num("".join(i)),end='')
print(":",end='')
for i in z[2:]:
    print(num("".join(i)),end='')
