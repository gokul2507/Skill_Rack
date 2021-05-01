def rotate(l,n,x):
    for i in range(x):
        l=[l[-1]]+l[:-1] 
    return l
