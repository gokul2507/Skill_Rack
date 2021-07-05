class IntegerList:
    def __init__(self,numList):
        self.numList=numList 
    def updateRange(self,l,r,x):
        for i in range(l-1,r):
            self.numList[i]+=x 
    def getSum(self,l,r):
        return sum(self.numList[l-1:r])