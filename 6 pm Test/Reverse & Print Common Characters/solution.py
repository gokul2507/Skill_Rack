s1,s2=input(),input()
s2=s2[::-1]
for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i]==s2[j] and i==j:
            print(s1[i],end="")