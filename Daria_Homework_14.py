class Unit:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.intellect = 1
        self.agility = 1
        self.force = 1

    def treatment(self):
        if self.health <= 90:
            self.health += 10
        elif 90 < self.health < 100:
            self.health = 100
   


    def increase(self, ): #### я полагаю, что можно было это сделать быстрее и не повторяться, но как...
        if self.skill == "intellect" and self.intellect <= 10:
            self.intellect += 1
        elif self.skill == "agility" and self.agility <= 10:
            self.agility += 1
        elif self.skill == "force" and self.force <= 10:
            self.force += 1



    def __repr__(self):
        return f"name:{self.name}, " \
                f"health:{self.health}, " \
                f"intellect:{self.intellect}, " \
                f"agility:{self.agility}, " \
                f"force:{self.force}"

class Mage(Unit):

    def __init__(self, name, magic):
        super().__init__(name)
        self.magic = magic
        self.skill = "intellect"

    def __repr__(self):
        return "Mage: " + super().__repr__() + f", magic:{self.magic}"


class Archer(Unit):

    def __init__(self, name, arc):
        super().__init__(name)
        self.arc = arc
        self.skill = "agility"


    def __repr__(self):
        return "Archer: " + super().__repr__() + f", arc:{self.arc}"

class Knight(Unit):

    def __init__(self, name, weapons):
        super().__init__(name)
        self.weapons = weapons

    def __repr__(self):
        return "Knight: " + super().__repr__() + f", weapons:{self.weapons}"


gendalf = Mage ("Gendalf", "water")
legolas = Archer("Legolas", "arbalet")
artur = Knight("Artur", "sword")


gendalf.increase()
gendalf.treatment()
gendalf.treatment()
legolas.increase()
print(gendalf)
print(legolas)
artur.treatment()
print(artur)



