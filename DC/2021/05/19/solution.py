class Test:
    def __init__(self,t,d):
        self.test=t 
        self.duration=d 
    def getName(self):
        return self.test 
    def getDuration(self):
        return self.duration
test1name = input().strip()
test1duration = int(input().strip())
test2name = input().strip()
test2duration = int(input().strip())
test1 = Test(test1name, test1duration)
test2 = Test(test2name, test2duration)
print(test1.getName() + " + " + test2.getName())
print(test1.getDuration()+test2.getDuration())