def reverse(l,n,x):
    for i in range(0,n-(n%x),x):
        l[i:i+x]=l[i:i+x][::-1]
    return l
