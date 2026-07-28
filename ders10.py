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


