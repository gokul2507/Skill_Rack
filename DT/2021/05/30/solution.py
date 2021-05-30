class FoodItem:
    def _init_(self,name,price):
        self.name=name
        self.price=price
    def _lt_(self,othr):
        return self.price<othr.price
    def _str_(self):
        return "%s:%d"%(self.name,self.price)