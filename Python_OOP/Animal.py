class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = 190

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health

class Dog(Animal):
    def __init__(self, name, health):
        self.health = 150
        super(Dog, self).__init__(name, health)

    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self, name, health):
        self.health = 170
        super(Dragon, self).__init__(name, health)

    def fly(self):
        self.health  -= 10

    def display_health(Animal):
        print "I am a Dragon"

dog1 = Dog("Dongwang", 170)
dog1.walk()
dog1.walk()
dog1.walk()
dog1.run()
dog1.run()
dog1.pet()
dog1.display_health()

dragon1 = Dragon("Faggot", 290)
dragon1.fly()
