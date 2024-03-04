class Food :
    def __init__(self, inputName : str,  inputHeal : int):
        self.name = inputName
        self.heal = inputHeal
        
class Animal :
    def __init__(self, inputName : str, inputColour : str , inputBlood : int):
        self.name = inputName
        self.colour = inputColour
        self.blood = inputBlood
    def showBlood(self):
        print(f"{self.name} darahnya sekarang {self.blood}")
    def hit(self, target):
        print(f"{self.name}  memukul {target.name}! darah berkurang 10")
        target.blood -= 10
    def sleep(self):
        print(f"{self.name} tidur") 
    def eat(self, food : Food):
        print(f"{self.name} makan {food.name}! darah bertambah {food.heal}")
        self.blood += food.heal
        

food1 = Food("Bayam", 40)
food2 = Food("Wortel", 60)
food3 = Food("Cabai", 20)

animal1 = Animal("Kucing", "White", 190)
animal2 = Animal("Anjing", "Black", 180)
animal3 = Animal("Kelinci", "Yellow", 170)

animal1.showBlood()
animal2.showBlood()
animal3.showBlood()

animal1.hit(animal2)
animal2.showBlood()

animal2.hit(animal3)
animal3.showBlood()

animal1.hit(animal3)
animal3.showBlood()

animal2.eat(food1)
animal2.showBlood() 

animal3.eat(food2)
animal3.showBlood()