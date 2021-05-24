class Stick:
    def _init_(self,lengthOfStick):
        self.lengthOfStick=lengthOfStick
    def _add_(self,new):
        return "Length: "+str(self.lengthOfStick+new.lengthOfStick)
        
stick1 = Stick(int(input().strip()))
stick2 = Stick(int(input().strip()))
stick3 = stick1 + stick2
print(stick3)
