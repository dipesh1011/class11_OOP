#Inheritance in 3 classed
class Country:
    def getinfo(self):
        self.name=input("Enter name of Country:")
        self.jern=input("Enter jersey number:")
        self.goal=input("Enter goal scored:")
    def showinfo(self):
        print("Country Name:",self.name)
        print("Country JerseyNumber:",self.jern)
        print("Goal:",self.goal)

class Club:
    def getdata(self):
        self.name1=input("Enter the name of the club:")
        self.jerseyn1=input("Enter the jerser number:")
        self.goal1=input("Enter the amount of goal scored:")
    def showdata(self):
        print("Club Name:",self.name1)
        print("Jerser number:",self.jerseyn1)
        print("Goal:",self.goal1)

class Player(Club):
    def getin(self):
        self.name2=input("Enter the name of the player:")
        Club.getdata(self)
    def showin(self):
        print("Player Name:",self.name2)
        print("***************************")
        Club.showdata(self)
        print("***************************")

c1=Country()
cl1=Club()
p1=Player()
p1.getin()
c1.getinfo()
p1.showin()
c1.showinfo()