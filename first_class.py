

class Mammal:
    def eat(self):
        print("Eats")
    
    def sleep(self):
        print("sleeps")


class Dog(Mammal):
     def bark(self):
         print("bark")

class Cat(Mammal):
    def meows(self):
        print("meows")


cat1 = Cat()
cat1.sleep()
cat1.meows()

dog1 = Dog()
dog1.bark()



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age    

#     def my_func(self):
#         print("Hello my name is "+ self.name)

# p1 = Person("John", "30")
# p1.my_func()