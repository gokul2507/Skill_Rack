class Fruit:
    count=0
    totalQuantity=0
    def __init__(self,s,n):
        self.s=s
        self.n=n
        Fruit.count+=1
        Fruit.totalQuantity+=n
    def __del__(self):
        Fruit.count-=1 
        Fruit.totalQuantity-=self.n 
    def __str__(self):
        return self.s+" : "+str(self.n)