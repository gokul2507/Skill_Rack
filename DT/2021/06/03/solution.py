class Player:
    def _init_(self,x,y):
        self.a=x
        self.b=y
    def _eq_(self,x):
        return self.b==x.b
    def _gt_(self,x):
        return self.b>x.b
    def _str_(self):
        return self.a+" "+str(self.b)
        
name, weight = input().strip().split()
player1 = Player(name, int(weight))
name, weight = input().strip().split()
player2 = Player(name, int(weight))
if player1 == player2:
    print(player1)
    print(player2)
elif player1 > player2:
    print(player1)
else:
    print(player2)
