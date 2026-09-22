#Create a base class animal and subclasses dog and cat
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Animal sounds")

class dog(Animal):
    def sound(self):
        print("Dog barks",self.name)

class cat(Animal):
    def sound(self):
        print("Cat meow's",self.name)

dog1=dog("Tim")
cat1=cat("Elly")

dog1.sound()
cat1.sound()


#Create a class hierarchy for Vehicle -> car -> Electric car
class Vehicle:
    def __init__(self,type):
        self.type=type
    def showtype(self):
        print("Vehicle type:",self.type)

class car(Vehicle):
    def __init__(self, type,brand):
        super().__init__(type)
        self.brand=brand
    def showcar(self):
        print("Car Brand:",self.brand)

class Electric_car(car):
    def __init__(self, type, brand,battery):
        super().__init__(type, brand)
        self.battery=battery
    def battery_type(self):
        print("Battery kwh:",self.battery)

car1= Electric_car("Ev","Tesla",50000)
car1.showtype()
car1.showcar()
car1.battery_type()


#Implement method overriding in a base and derived class
class Animals:
    def sound(self):
        print("Animal makes a sound")
class Dogs(Animals):
    def sound(self):
        print("Dog bark's")

animal1=Animals()
dog1=Dogs()

animal1.sound()
dog1.sound()


#Demonstrate multiple inheritence with two parent classes
class Father:
    def show_father(self):
        print("This is Father class")
class Mother:
    def show_mother(self):
        print("This is mother class")
class Child(Father,Mother):
    def show_child(self):
        print("This is child class")

child1=Child()
child1.show_father()
child1.show_mother()
child1.show_child()


#Create a polymorphic function that works with the different shapes
class shapes:
    def area(self):
        print("Area of a shape:")
class circle(shapes):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14* (self.radius**2)

class rectangle(shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length * self.width

def calculate_area(shapes):
    print("Area:",shapes.area())

cir=circle(6)
rec=rectangle(10,15)

calculate_area(cir)
calculate_area(rec)


#Create a bank system with Savingsaccount and currentaccount classes
class bankacc:
    def acc_type(self):
        print("This is a bank account")

class Savingsacc(bankacc):
    def acc_type(self):
        print("This is a savings account")

class currentacc(bankacc):
    def acc_type(self):
        print("This is current account")

savings=Savingsacc()
current=currentacc()

savings.acc_type()
current.acc_type()


#Create a class with private attributes and getter/setter methods
class student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks

    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks

    def set_name(self,name):
        self.__name=name

    def set_marks(self,marks):
        self.__marks=marks

student1=student("Rahul",89)

print("Name:",student1.get_name())
print("Marks:",student1.get_marks())

student1.set_name("Amit")
student1.set_marks(99)

print("Updated name:",student1.get_name())
print("Updated marks:",student1.get_marks())


#Create a teacher and student class to show inheritence
class Teacher:
    def __init__(self,name):
        self.name=name
    def teach(self):
        print(self.name,"is teaching")
class students(Teacher):
    def study(self):
        print(self.name,"is studying")

student2=students("Akash")
student2.teach()
student2.study()


#Create a musicplayer class and subclass spotify to override play method
class musicplayer:
    def play(self):
        print("Playing music")

class spotify(musicplayer):
    def play(self):
        print("Playing music on spotify")

sp1=spotify()
sp1.play()


#Demonstrate the use of super() in inheritance
class Parent:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display(self):
        super().show()
        print("Age:", self.age)        

child1 = Child("Hem", 20)

child1.display()