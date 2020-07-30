
class Animal():
    def __init__(self, name, color, age):
        self.name= name
        self.color =  color
        self.age= age
    def call(self, type):
        print(type)

class Dog(Animal):
    def __init__(self, name, color, age):
        Animal.__init__(self, name, color, age)

    def call(self , call):
        print('BARK')

class Cat(Animal):
    def __init__(self, name, color, age):
        Animal.__init__(self, name, color, age)

    def call(self , call):
        print('Miao')
