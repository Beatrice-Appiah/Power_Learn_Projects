# Activity 1:
class Book:
    colour = "Black"
    pages = 91
    size = "big size"
    title = "The Adventures Kwesi Beyeden"

    def read (self):
        print("\nThe book is very interesting")
    def outlook (self):
        print("\nThe book is {colour}")
    def count_pages (self):
        print("\nThe book has {pages} leaflets.")
    def sell (self):
        print ("\nThe best-seller book this year is titled {title} and it made over a million sales.")

def __init__ (self, colour,pages,size,title):
    self.colour = colour
    self.pages = pages
    self.size = size
    self.title = title
    
book1 = ("Pink", 56, "medium size", "The Mysterious Cleopas")
book2 = ("White", 10, "small size", "Snow White")
book3 = ("Olive Green", 77, "medium size", "Kweku Ananse and the land of Fools")

# (C) Polymorphism 
class Novel(Book):
    def __init__(self, colour,rate ):
        super().__init__(colour) 
        self.rate = rate
    
    def read (self):
        """Overrides the read method for Novel"""
    print("I really love this the plot of this fiction")


class Fantasy(Book):
    def __init__(self, colour, type):
        super().__init__(colour)
        self.type = type

    def read (self):
        print("This book completed no picture")

# Creating objects of different types
my_novel = Novel("Yellow", "50%" )
my_fantasy = Fantasy("Turquoise", "poem")

# Polymorphism in action: The correct speak method is called based on the object's type
my_novel.read()
my_fantasy.read()


#(D) Encapusulation
class Book:
    def __init__(self, title, author, price):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self.__price = price  # Private attribute (using double underscore)

    # Getter method for price
    def get_price(self):
        return self.__price

    # Setter method for price (with validation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be a positive number.")

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: ${self.get_price()}"

book = Book("Encapsulation in Python", "Jane Doe", 25)
print(book.display_info())

# Using the setter method to modify price safely
book.set_price(30)
print(book.display_info())





# Activity 2: (Polymorphism)
class Vehicle:
    def move(self):
        pass  # Placeholder method (to be overridden)

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
