class Date:
    def _init_(self,y,m='Jan',d=1):
        self.y=y
        self.m=m
        self.d=d
    def _str_(self):
        return "%02d"%(self.d)+"-"+self.m+"-"+"%04d"%(self.y)