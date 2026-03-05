class Car:
    def drive(this):
        print("Більше газу. Менше ям.")

car = Car()

car.drive()

class MiniPig:
    def speak(this):
        print("Хрю хрю ...")

class Dog(MiniPig):
    def speak(this):
        print("Гав, гав, хрю")

pig = MiniPig()
pig.speak()

dog = Dog()
dog.speak()

myFriends = [MiniPig(), Dog()]

for obj in myFriends:
    obj.speak()

def talk(obj):
    obj.speak()

talk(MiniPig())
talk(Dog())
