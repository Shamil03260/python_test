# class
# __init__ - constructor
# __str__ - her hanso metodun adini qaytarir
# __dict__ - Python-da obyektin bütün atributlarını saxlayan lüğətdir 
# inheritance -   Inheritance (miras) — bir class-ın başqa bir class-ın xüsusiyyətlərini və metodlarını miras almasıdır.  

# class Student:
#     pass

# student1 = Student()


# class Student:

#     def say_hello(self):
#         print("Salam")
        
    
        
        
# student = Student()

# student.say_hello()



# class Student:
    

#     def say_hello(self):
#         print("Salam")

#     def study(self):
#         print("Dərs oxuyuram")

#     def exam(self):
#         print("İmtahan verirəm")


# student = Student()

# student.say_hello()
# student.study()
# student.exam()



# class Student:

#     def __init__(self, name, email, age, score):
#         print("Yeni tələbə yaradıldı")
        

# student = Student("Veli", "test@gmail.com", 20, 90)


# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def show(self):
#         return f"{self.age} | {self.name}"
        
    

# student = Student("Test", 60)
# student = student.show()
# print(student)

# class Student:

#     def __init__(self,name):
#         self.name=name
        
#     def __str__(self):
#         return self.name    

# student=Student("Əli")


# print(student)


# class Student:

#     def __init__(self,name,age):

#         self.name=name

#         self.age=age

#     def __str__(self):

#         return f"Ad: {self.name}, Yaş: {self.age}"
    
# student=Student("Əli",20)


# print(student.__dict__)
# print(student)




# class Student:

#     pass

# student = Student()

# student.name = "Əli"

# student.age = 20
# print(student.__dict__)


# Inheritance 
# class Parent():
    
#     # class variable
#     university = "Oxford"
#     # Instance Variable  -  name, surname
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
       
        
#     def show(self):
#         return f" {self.name } {self.surname}"
    

# class Child(Parent):
#     pass

# b = Child("Ali","Aliyev")


# print(b.show())


# print(b.university)


# class taskları

# task 1

class Car:
    def __init__(self, marka, model, il):
        self.marka = marka
        self.model = model
        self.il = il
        
    def drive(self):
        return f"{self.marka} {self.model} hərəkət edir."

car1 = Car("BMW", "X5", 2020)
print(car1.drive())


# task 2

class Person:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        
    def is_adult(self):
        if self.yas >= 18:
            return f"{self.ad} Yetkindir."
        else:
            return f"{self.ad} Yetkin deyil."
        
person1 = Person("Ali", 20)
print(person1.is_adult())


# task 3

class Student:
    def __init__(self, ad, bal):
        self.ad = ad
        self.bal = bal
        
    def passed(self):
        if self.bal >= 50:
            return f"{self.ad} keçdi."
        else:
            return f"{self.ad} keçmədi."
        
student1 = Student("Ali", 60)
print(student1.passed())


# task 4

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def topla(self):
        return self.a + self.b
    
    def cix(self):
        return self.a - self.b
    
    def vur(self):
        return self.a * self.b
    
    def bol(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Sıfıra bölmə mümkün deyil!"
        
calc = Calculator(10, 5)
print(calc.topla())
print(calc.cix())
print(calc.vur())
print(calc.bol())


# task 5

class RandomPassword:
    def __init__(self):
        pass
    
    def generate_password(self, length=8):
        import random
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def show_password(self):
        password = self.generate_password()
        return f"Təsadüfi şifrə: {password}"
    
password_generator = RandomPassword()
print(password_generator.show_password())
    
    
# task 6

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        return f"{self.title} filmi {self.duration} dəqiqədir."


class Hall:
    def __init__(self, name, seats):
        self.name = name
        self.seats = seats


class Seat:
    def __init__(self, number):
        self.number = number
        self.is_reserved = False

    def reserve(self):
        if not self.is_reserved:
            self.is_reserved = True
            return f"{self.number} nömrəli yer rezerv edildi."
        else:
            return f"{self.number} nömrəli yer artıq rezerv olunub."


class Customer:
    def __init__(self, name):
        self.name = name

    def reserve_seat(self, seat):
        if not seat.is_reserved:
            seat.is_reserved = True
            return f"{self.name} {seat.number} nömrəli yeri rezerv etdi."
        else:
            return f"{seat.number} nömrəli yer artıq rezerv olunub."


class Cinema:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, duration):
        movie = Movie(title, duration)
        self.movies.append(movie)

    def show_movies(self):
        for movie in self.movies:
            print(movie.show_info())


cinema = Cinema()


cinema.add_movie("Avatar", 162)
cinema.add_movie("Titanic", 195)
cinema.add_movie("Interstellar", 169)


cinema.show_movies()


hall = Hall("A zalı", 100)


seat1 = Seat(1)
seat2 = Seat(2)


customer = Customer("Ali")


print(customer.reserve_seat(seat1))
print(customer.reserve_seat(seat1))
print(customer.reserve_seat(seat2))