#Nama : Elsa Elisa Yohana Sianturi
#NIM : 122140135

class Food :
    def __init__(self, inputName : str, inputHeal : int) :
        self.name = inputName
        self.heal = inputHeal
class Robot :
    def __init__(self, inputName : str, inputLife : int) :
        self.name = inputName
        self.life = inputLife
    def showLife(self) :
        print(f"{self.name} nyawanya sekarang {self.life}")
        print(" ")
    def hit(self, target1) :
        print(f"{self.name} memukul {target1.name} ! Nyawa berkurang 20")
        print(" ")
        target1.life -= 20
    def kick(self, target2) :
        print(f"{self.name} menendang {target2.name} ! Nyawa berkurang 40")
        print(" ")
        target2.life -= 40
    def eat(self, food : Food) :
        print(f"{self.name} makan {food.name} ! Darah bertambah {food.heal}" )
        self.life += food.heal
        print(" ")
        
        
        
food1 = Food("Carrot", 50)
food2 = Food("Broccoli", 20)
food3 = Food("Spinach", 10)

robot1 = Robot("Optimus", 120)
robot2 = Robot("Bumblebee", 180)
robot3 = Robot("Mirage", 120)
robot4 = Robot("Arcee", 80)

robot1.showLife()
robot2.showLife()
robot3.showLife()
robot4.showLife()

robot1.kick(robot4)
robot4.showLife()

robot3.hit(robot4)
robot4.showLife()

robot2.hit(robot4)
robot4.showLife()

robot4.eat(food1)
robot4.showLife()

robot4.eat(food2)
robot4.showLife()

robot4.kick(robot2)
robot2.showLife()


