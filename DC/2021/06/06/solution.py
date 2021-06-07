class Rectangle:
    rectangleCount=0
    totalArea=0
    def __init__(self,l,b):
        self.l=l 
        self.b=b 
        Rectangle.rectangleCount+=1 
        Rectangle.totalArea+=self.l*self.b 
    def __del__(self):
        Rectangle.rectangleCount-=1 
        Rectangle.totalArea-=self.l*self.b 
    def __repr__(self):
        return "Length={}, Breadth={}, Area={}".format(self.l,self.b,self.l*self.b)
N = int(input())
rectangles = []
for ctr in range(N):
    length, breadth = map(int, input().split())
    rectangles.append(Rectangle(length, breadth))
X = int(input())
print(Rectangle.rectangleCount)
print(Rectangle.totalArea)
del rectangles[X-1]
for rect in rectangles:
    print(rect)
print(Rectangle.rectangleCount)
print(Rectangle.totalArea)