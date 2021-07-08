while 1:
    try :
        s = input().strip()
        a = ""
        for i in s:
            if i not in "1234567890":
                a+=i
            else:
                break
        if a:
            print(a)
        else:
            print(-1)
    except:
        break