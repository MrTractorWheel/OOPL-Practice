class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def printPoint(self):
        return (self.x,self.y)
    def distance(self):
        x = self.x
        y = self.y
        t= x*x+y*y
        d = str(t)
        return "sqrt of " + d

class Person:
    def __init__(self, age=None, name=None):
        self.age = age
        self.name = name
    def getAge(self): return self.age
    def getName(self): return self.name
    def setAge(self,age): self.age = age
    def setname(self,name): self.name = name
    def greet(self): print("I'm %s, I'm %i years old"%(self.name,self.age))

class Student(Person):
    def __init__(self, age=None, name=None, uni=None, ID=None):
        Person.__init__(self,age,name)
        self.uni = uni
        self.ID = ID
    def greet(self):
        Person.greet(self)
        print ("Univercity %s, ID: %s"%(self.uni,self.ID))
