
class Pet:
    def __init__(self, name , type , tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 10
        self.sound = sound
        self.ninjas_pet = Ninja

    def sleep(self):
        print('Zzzz Zzzz')
        self.energy = self.energy + 25
        print(f"{self.name}'s energy is now {self.energy}")
        return self

    def eat(self):
        print('Nom nom nom')
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f'{self.name} ate some food!')
        print(f"{self.name}'s energy and health are now {self.energy} and {self.health}")
        return self

    def play(self):
        print(f'rawwr {self.name} jumps around')
        self.health = self.health + 5
        print(f"{self.name}'s health is now {self.health}")
        return self

    def noise(self):
        print(self.sound)
        return self

class Ninja:
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.ninjas_pet = pet #why doesnt Pet work but pet does? is it because 
                            #jacks_dragon micheal is the instance of pet when defining ninja_1?
                            #super confused why i cant associate self.ninjas_pet to the class Pet like we did
                            #with the bank account thing
        
    def walk(self):
        print(f'lets go for a walk {self.ninjas_pet.name}')
        self.ninjas_pet.play()
        return self

    def feed(self):
        print(f'time to eat {self.ninjas_pet.name}')
        self.ninjas_pet.eat()
        return self

    def bathe(self):
        print(f'time for a bath {self.ninjas_pet.name}')
        self.ninjas_pet.noise()
        return self

jacks_dragon_porky = Pet('porky','dragon','flip','rawr')

ninja_1 = Ninja('jack','piro',jacks_dragon_porky,'humans','sheep')

ninja_1.walk().feed().bathe()

