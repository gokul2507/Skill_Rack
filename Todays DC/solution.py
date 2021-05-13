import re
def get(x):
    return int("".join(re.findall("[0-9]",x))),re.findall("[a-zA-Z]",x)[0],
for i in sorted(map(get,input().split("-"))):
    print(end=i[1])