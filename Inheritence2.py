class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(self.name,"give me food meow")
class Cat(Animal):
    def meow(self):
        print(self.name,"meow,meow,billi")
cat1=Cat("pusshy")
cat1.eat()
cat1.meow()