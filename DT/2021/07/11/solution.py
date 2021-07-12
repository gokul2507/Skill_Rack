number,word=[''],['']
for i in input().strip():
    if i.isdigit():
        number[-1]+=i
        if word[-1]:
            word.append('')
    else:
        word[-1]+=i
        if number[-1]:
            number.append('')
number=number[:-1]
for i in range(len(number)):
    print((" ".join(word[i:])+" ")*int(number[i]))