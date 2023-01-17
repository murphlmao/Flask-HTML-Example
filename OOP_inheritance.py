class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("Some animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")
           
class Cat(Animal):
    def speak(self):
        super().speak()
        print("Meow!")

dog = Dog("Fido")
cat = Cat("Whiskers")

#print(dog.name) # Output: Fido
#print(cat.name) # Output: Whiskers

dog.speak() # Output: Some animal sound\nWoof!
print() # blank line
cat.speak() # Output: Some animal sound\nMeow!
