try:
    while 1:
        s=0
        for i in input().split():
            try:
                s+=int(i)
            except:
                break
        print(s)
except:
    pass