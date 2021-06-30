class Distance:
    def __init__(self,a,b):
        self.f=a 
        self.i=b 
    def __add__(self,x):
        f1=self.f+x.f 
        i1=self.i+x.i 
        return Distance(f1+i1//12,i1%12) 
    def __str__(self):
        return str(self.f)+" "+str(self.i) 
    def addInches(self,x): 
        self.f=self.f+(self.i+x)//12 
        self.i=(self.i+x)%12