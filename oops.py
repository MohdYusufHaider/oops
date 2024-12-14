#Q1> Explain the importance of Functions?
#Ans >>> Avoid Reundancy,Readability,Mainitainace easily,

#Q2 Write a basic function to greet students?
def greet_student(name):
    print(f"Hello, {name}! Welcome to the class.")

greet_student("Alice")

#Q3>0 What is the difference between print and return statements?
#print: Displays output to the console but does not allow further use of the value.
#return: Sends a value back to the caller, enabling further computation.
#0 What are *args and **kwargs?
#Ans>*args: Allows passing a variable number of positional arguments.

#**kwargs: Allows passing a variable number of keyword arguments.
#Q5>Explain the iterator function?
#Ans>> Iteration function allow looping over element sequently.

#Q6>0 Write a code that generates the squares of numbers from 1 to n using a generator?
def generate_squares(n):
    for i in range(1, n+1):
        yield i ** 2

for square in generate_squares(5):
    print(square)

#Q7>Write a code that generates palindromic numbers up to n using a generator?
def generate_palindromes(n):
    for i in range(n + 1):
        if str(i) == str(i)[::-1]:
            yield i

for pal in generate_palindromes(100):
    print(pal)

#Q8>Write a code that generates even numbers from 2 to n using a generator0
def generate_evens(n):
    for i in range(2, n + 1, 2):
        yield i

for even in generate_evens(10):
    print(even)

#Q9> Write a code that generates powers of two up to n using a generator?
def generate_powers_of_two(n):
    for i in range(n + 1):
        yield 2 ** i

for power in generate_powers_of_two(5):
    print(power)

#Q10> Write a code that generates prime numbers up to n using a generator?
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i

for prime in generate_primes(20):
    print(prime)

#Q11>Write a code that uses a lambda function to calculate the sum of two numbers?
add = lambda x, y: x + y
print(add(3, 4))


#Q12>Write a code that uses a lambda function to calculate the square of a given number0
square = lambda x: x ** 2
print(square(5))

#Q13>Write a code that uses a lambda function to check whether a given number is even or odd?
check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even_odd(4))

#Q15>Write a code that uses a lambda function to concatenate two strings?
concat = lambda x, y: x + y
print(concat("Hello, ", "World!"))

#Q16>Write a code that uses a lambda function to find the maximum of three given numbers?
max_of_three = lambda x, y, z: max(x, y, z)
print(max_of_three(3, 7, 5))

#Q17>Write a code that calculates the product of positive numbers from a given list?
from functools import reduce

nums = [1, -2, 3, 4, -5]
product = reduce(lambda x, y: x * y, filter(lambda x: x > 0, nums))
print(product)

#Q18>Write a code that doubles the values of odd numbers from a given list?
nums = [1, 2, 3, 4, 5]
doubled_odds = [x * 2 for x in nums if x % 2 != 0]
print(doubled_odds)

#Q19>Write a code that calculates the sum of cubes of numbers from a given list?
nums = [1, 2, 3]
sum_of_cubes = sum(x ** 3 for x in nums)
print(sum_of_cubes)

#20> Write a code that filters out prime numbers from a given list?
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_primes = [x for x in nums if is_prime(x)]
print(filtered_primes)

#Q21>Write a code that uses a lambda function to calculate the sum of two numbers?
add = lambda x, y: x + y
print(add(3, 5))  

#Q22>Write a code that uses a lambda function to calculate the square of a given number?

square = lambda x: x ** 2
print(square(4))  

#Q23> Write a code that uses a lambda function to check whether a given number is even or odd?
is_even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even_or_odd(7))  

#Q24>Write a code that uses a lambda function to concatenate two strings?
concat = lambda str1, str2: str1 + str2
print(concat("Hello, ", "World!")) 

#Q25>Write a code that uses a lambda function to find the maximum of three given numbers?
max_of_three = lambda x, y, z: max(x, y, z)
print(max_of_three(3, 7, 5))  
#Q26>0 What is encapsulation in OOP?
#Ans

#Q27>Explain the use of access modifiers in Python classes?
#Ans It controls the visibility of class member 

#Q28>What is inheritance in OOP?
#Inheritance allows a class (child) to inherit attributes and methods from another class (parent)

#Q29>Define polymorphism in OOP?
#ANS>Polymorphism allows objects of different classes to be treated as instances of the same class through shared methods

#Q30> Explain method overriding in Python?
#Ans>Method overriding allows a child class to provide a specific implementation for a method inherited from a parent class.

#Q31>Define a parent class Animal with a method make_sound that prints "Generic animal sound". Create a
#child class Dog inheriting from Animal with a method make_sound that prints "Woof!
class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

dog = Dog()
dog.make_sound()  

#Q32>Define a method move in the Animal class that prints "Animal moves". Override the move method in the
#Dog class to print "Dog runs
class Animal:
    def move(self):
        print("Animal moves")

class Dog(Animal):
    def move(self):
        print("Dog runs")

dog = Dog()
dog.move()  

#Q33>Create a class Mammal with a method reproduce that prints "Giving birth to live young." Create a class
#DogMammal inheriting from both Dog and Mammal?

class Mammal:
    def reproduce(self):
        print("Giving birth to live young")

class Dog:
    def make_sound(self):
        print("Woof!")

class DogMammal(Dog, Mammal):
    pass

dm = DogMammal()
dm.make_sound()  
dm.reproduce()   

#Q35> Create a class GermanShepherd inheriting from Dog and override the make_sound method to print
#"Bark!8
class Dog:
    def make_sound(self):
        print("Woof!")

class GermanShepherd(Dog):
    def make_sound(self):
        print("Bark!")

gs = GermanShepherd()
gs.make_sound()  # Output: Bark!

#Q36>Define constructors in both the Animal and Dog classes with different initialization parameters?
class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

dog = Dog("Canine", "Labrador")
print(dog.species)  
print(dog.breed)    

#Q36> What is abstraction in Python? How is it implemented?
#Abstraction is the process of hiding implementation details and exposing only necessary functionality. In Python, it can be implemented using abstract classes and the abc module.

#Q37Explain the importance of abstraction in object-oriented programming?
#Ans >.Simplifies comlexitiy,Promotes modular design,improves maintainability,resuable codes

#Q39>How are abstract methods different from regular methods in Python?
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

c = Car()
c.drive()

#Q40>How can you achieve abstraction using interfaces in Python?
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

def render_shape(shape):
    shape.draw()

render_shape(Circle())  
render_shape(Square())  

#Q41>How does Python achieve polymorphism through method overriding?
class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

def make_sound(animal):
    animal.sound()

make_sound(Dog())  

#Q43>. Describe how Python supports polymorphism with duck typing?

class Cat:
    def sound(self):
        print("Meow!")

class Dog:
    def sound(self):
        print("Woof!")

def make_sound(animal):
    animal.sound()  

make_sound(Cat())
make_sound(Dog())  

#Q47>How do you achieve encapsulation in Python?
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance()) 

#Q48> Can encapsulation be bypassed in Python? If so, how?
#YES
account = BankAccount(1000)
print(account._BankAccount__balance)  # Access private attribute (discouraged)

#Q49>Develop a Person class with private attributes name and email, and methods to set and get the email?
class Person:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

p = Person("virat", "virat@example.com")
p.set_email("virat@example.com")
print(p.get_email())  
#Q51Why is encapsulation considered a pillar of object-oriented programming (OOP)?
#ans >
#Protects data integrity.
#Restricts unauthorized access.
#Facilitates maintenance by providing controlled access methods.
#Encourages modular design through well-defined interfaces.

#Q52>>Create a decorator in Python that adds functionality to a simple function by printing a message before
#and after the function execution?
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#Q53>Modify the decorator to accept arguments and print the function name along with the message?
def my_decorator_with_args(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{message} - Function '{func.__name__}' is starting.")
            result = func(*args, **kwargs)
            print(f"{message} - Function '{func.__name__}' has finished.")
            return result
        return wrapper
    return decorator

@my_decorator_with_args("INFO")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#Q54>Create two decorators, and apply them to a single function. Ensure that they execute in the order they are
#applied?
def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper

@decorator_one
@decorator_two
def greet():
    print("Hello!")

greet()

#Q55> Modify the decorator to accept and pass function arguments to the wrapped function?
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Bob")

#Q56>Create a decorator that preserves the metadata of the original function?

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing function")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """This is an example function."""
    print("Hello!")

print(example.__name__)    
print(example.__doc__)     

#Q57>Create a Python class `Calculator` with a static method `add` that takes in two numbers and returns their
#sum?
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(3, 7))  # Output: 10

#Q58>Create a Python class `Employee` with a class `method get_employee_count` that returns the total
#number of employees created?
class Employee:
    employee_count = 0

    def __init__(self):
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

emp1 = Employee()
emp2 = Employee()
print(Employee.get_employee_count())  

#Q59>Create a Python class `StringFormatter` with a static method `reverse_string` that takes a string as input
#and returns its reverse?
class StringFormatter:
    @staticmethod
    def reverse_string(s):
        return s[::-1]

print(StringFormatter.reverse_string("hello"))  

#Q60>.Create a Python class `Circle` with a class method `calculate_area` that calculates the area of a circle
#given its radius?
class Circle:
    pi = 3.14

    @classmethod
    def calculate_area(cls, radius):
        return cls.pi * radius * radius

print(Circle.calculate_area(5))  

#Q61> Create a Python class `TemperatureConverter` with a static method `celsius_to_fahrenheit` that converts
#Celsius to Fahrenheit
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))  

#Q62>What is the purpose of the __str__() method in Python classes? Provide an example?
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person(name={self.name})"

p = Person("Alice")
print(p) 

#Q63>How does the __len__() method work in Python? Provide an example?
class Collection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

c = Collection([1, 2, 3])
print(len(c))  

#64>Explain the usage of the __add__() method in Python classes. Provide an example?
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

n1 = Number(3)
n2 = Number(5)
result = n1 + n2
print(result.value) 

#Q65>What is the purpose of the __getitem__() method in Python? Provide an example?
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

my_list = MyList([10, 20, 30])
print(my_list[1]) 

#Q66>Explain the usage of the __iter__() and __next__() methods in Python. Provide an example using
#iterators?
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current
        else:
            raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)

#Q67>/ Explain the role of setter methods in Python. Demonstrate how to use a setter method to modify a class
#attribute using property decorators?
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

p = Person("Alice")
p.name = "Bob"
print(p.name)  

#Q69>What is the purpose of the @property decorator in Python? Provide an example illustrating its usage?
#Ans>.

#The @property decorator in Python allows you to define a method as a getter for an attribute, 
#enabling you to access it like a regular attribute (without calling the method). This helps in implementing encapsulation by controlling access to an attribute, while still using a clean syntax
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Height must be positive")

    @property
    def area(self):
        return self._width * self._height

# Creating an instance of Rectangle
rect = Rectangle(5, 10)

# Accessing width and height like regular attributes
print(rect.width)   # Output: 5
print(rect.height)  # Output: 10

# Modifying width and height using setters
rect.width = 8
rect.height = 15

# Accessing the computed property 'area'
print(rect.area)  # Output: 120

# Attempting to set a negative value (will raise an error)
try:
    rect.width = -3
except ValueError as e:
    print(e)  # Output: Width must be positive













#Q70>Explain the use of the @deleter decorator in Python property decorators. Provide a code example
#demonstrating its application?
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name...")
        self._name = None

p = Person("Alice")
del p.name
print(p.name)  

#Q71>How does encapsulation relate to property decorators in Python? Provide an example showcasing
#encapsulation using property decorators?
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid balance")

account = BankAccount(100)
print(account.balance)
account.balance = 200
print(account.balance)  







