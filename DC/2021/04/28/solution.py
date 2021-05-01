def color(color_1,color_2):
    if color_1==color_2:
        return color_1
    color_1,color_2=sorted([color_1,color_2])
    if color_1=="B":
        if color_2=="G":
            return "C"
        else:
            return "M"
    return "Y"
row,col=map(int,input().split())
z=[input().split() for _ in range(row)]
for R in z:
    for C in range(col//2):
        print(color(R[C],R[-C-1]),end=' ')
    print()
