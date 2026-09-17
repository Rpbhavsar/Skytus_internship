#Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.
class car:
    def __init__ (self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed
    def accelerate(self):
        self.speed += 10
        print("Car accelerated. Current speed:", self.speed, "km/h")

    def brake(self):
        self.speed = 0
        print("Car brake. Current speed:",self.speed,"km/h")

car1 = car("Toyota","innova",50)
print(car1.model)
car1.accelerate()
car1.brake()


#Create a BankAccount class with deposit and withdraw methods.
class Bankaccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print("Balance after withdraw:", self.balance)

    def deposite(self, amount):
        self.balance += amount
        print("Balance after deposite:", self.balance)


amt = Bankaccount(1000)

amt.withdraw(200)
amt.deposite(100)


#Create a student class with a method to calculate average marks
class student:
    def __init__ (self,marks):
        self.marks=marks
    def avgmarks(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average marks:",avg)

std1=student([100,99,89,70,89])
std1.avgmarks()


#Create a rectangle class with methods to find the area and perimenter
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        area= self.length*self.width
        print("Area of rectangle:",area)

    def perimeter(self):
        peri = 2*(self.length + self.width)
        print("Perimeter of rectangle:",peri)

rect=rectangle(20,30)
rect.area()
rect.perimeter()


#Create an employee class that displays salary details
class employee:
    def __init__(self,salary):
        self.salary=salary

    def display(self):
        print("Salary:",self.salary)

emp=employee(100000)
emp.display()


#Create a book class to store title, author, price and display details
class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print("Book title:",self.title)
        print("Author name:",self.author)
        print("Book price:",self.price)

book1=book("Hero","Ruskin bond",200)
book1.display()


#Create a circle class to find its area and circumference
class circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        area =3.14*(self.radius)**2
        print("Area of circle:",area)

    def circumference(self):
        cir=2*(3.14*self.radius)
        print("Circumference of circle:",cir)

circle1=circle(30)
circle1.area()
circle1.circumference()


#Create a laptop class with a method to apply discount on price
class laptop:
    def __init__(self,price):
        self.price=price

    def discount(self):
        disc= self.price - (10/100 *self.price)
        print("Price after discount:",disc)

lap=laptop(100000)
lap.discount()


#Create a flight class with seat booking functionality
class flight:
    def __init__(self,totalseats,bookseat):
        self.totalseats=totalseats
        self.bookseat=bookseat

    def available(self):
        print("Total seats available:",self.totalseats)

    def seatbooked(self):
        seat= self.totalseats-self.bookseat
        print("Available seat after booking:",seat)

flight1=flight(200,30)
flight1.available()
flight1.seatbooked()


#Create a shop class with a method to add and list products
class shop:
    def __init__(self):
        self.products=[]

    def addproduct(self,product):
        self.products.append(product)
        print("Product added:",product)

    def listproduct(self):
        print("product in shop:")
        for product in self.products:
            print(product)

shop1=shop()
shop1.addproduct("mobile")
shop1.addproduct("Laptop")
shop1.addproduct("Tv")
shop1.listproduct()