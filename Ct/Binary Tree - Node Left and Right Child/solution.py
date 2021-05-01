class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def add(root,data):
    if root==None:
        return node(data)
    elif root.data>data:
        root.left=add(root.left,data)
    else:
        root.right=add(root.right,data)
    return root
def prin(root,data):
    if root==None:
        return
    if root.data==data:
        t=""
        if root.left:
            t+=str(root.left.data)+" "
        if root.right:
            t+=str(root.right.data)
        if not t:
            t='-1'
        print(t)
        exit()
    prin(root.left,data)
    prin(root.right,data)
r=None
l=list(map(int,input().split()))
for i in l:
    r=add(r,i)
prin(r,int(input()))
