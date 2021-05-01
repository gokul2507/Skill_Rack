class solution:
    def _init_(self):
        self.string=input().split()
        self.n=int(input())
        self.z=[["*" for _ in range(self.n*4)] for __ in range(self.n*3)]
    def put(self,r,k,c):
        for i in range(r,r+self.n):
            for j in range(k,k+self.n):
                self.z[i][j]=c
    def assign(self):
        self.put(self.n,self.n,self.string[0])
        self.put(self.n,self.n*2,self.string[1])
        self.put(self.n,self.n*3,self.string[2])
        self.put(self.n,0,self.string[3])
        self.put(0,self.n,self.string[5])
        self.put(self.n*2,self.n,self.string[4])
    def display(self):
        for i in self.z:
            print(*i)
q=solution()
q.assign()
q.display()
