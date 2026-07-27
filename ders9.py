# def salam():
#     return "Welcome"    
    
    
# x = salam()
# print(x)


#  a ve be parametr
# def topla(a,b):
#     return a ** b

# #  2 ve 3 argument
# x = topla(2, 3)
# print(x)



# def salam(ad):
#     print(ad)
    
# salam("Nurlan")



# def topla(a,b):
#     return a + b

# x = topla(5 , 1)

# print(x)


# Positional Arguments parameter1 , parameter2
# def funksiya(parameter1, parameter2):
#     return parameter1 + parameter2


# x = funksiya(5 , 1)

# print(x)


# def melumat(ad, yas):
#     print(ad)
#     print(yas)

# melumat(20 ,  "test")



# Keyword Arguments ad,yas,city,number,my_bool,country,activate
# def create_user(ad,yas,city,number,my_bool,country,activate):
#     print(ad,yas,city,number,my_bool,country,activate)


# create_user(
#     ad="Murad",
#     yas=22,
#     city = "Bakı",
#     country= "Azərbaycan",
#     my_bool= True,
#     activate =False,
#     number = 5000
# )



# def login(username, password, remember):
#     pass

# login(

#     username="admin",

#     password="12345",

#     remember=True

# )
 
 
# default Arguments
# Default argument həmişə sonda yazılır.
# def my_function(x=5):
#     return x + 5

# my_func = my_function(10)
# print(my_func)


# def info(ad="Unknown",

#          yas=0,

#          seher="Yoxdur"):

#     print(ad)

#     print(yas)

#     print(seher)



# info("test",40,"baki")


# Default və Positional birlikdə
# def info(ad, yas=18):

#     print(ad)

#     print(yas)

# info(30,"Murad")


# Positional + Keyword birlikdə 
# Python-da positional argument-lər həmişə əvvəl, keyword argument-lər isə sonra gəlməlidir.
# def info(ad,yas,seher):

#     print(ad,yas,seher)

# info("Murad", yas=22, seher="Bakı")

# info(ad="Murad",22,"Bakı")


# *args - positional arguments - tuple qaytarir
# def cem(*args):
#     return sum(args)

# x = cem(5, 10, 20, 30, 40)
# print(x)

# def cem(*args):
#     print(args[2])
    
# cem(5, 10, 15)

# ----

# **kwargs - keyword arguments - dict qaytarir
# def info(**kwargs):
#     print(kwargs.values())

# info(ad="Murad", yas=22, city="Baki")

# global variable
# a = 0

# def my_function(x, y):
#     # local variable
#     i = 5 
#     return x + y
    

# print(i)


# nested function
# def outer_function(x):

#     def inner_function(y):
#         return y * 2

#     result = inner_function(x)

#     return result


# output = outer_function(100)

# print(output)


# def sifre_yoxla(sifre):

#     if len(sifre) >= 8:
#         return "Güclü şifrə"

#     else:
#         return "Zəif şifrə"


# print(sifre_yoxla("abc123"))
# print(sifre_yoxla("Python123"))



# lamdba


# Lambda Syntax
# lambda parametr: ifadə

# kvadrat = lambda x: x * x

# # def ile Əslində bu kod
# def kvadrat(x):
#     return x * x



# cem = lambda a, b: a + b

# print(cem(5,10))


# hesabla = lambda a,b,c: a*b+c

# print(hesabla(2,3,4))



# ededler = [1,2,3,4]

# def kvadrat(x):
#     return x*x

# netice = map(kvadrat, ededler)

# print(list(netice))


# ededler = [1,2,3,4]

# netice = map(lambda x: x*x, ededler)

# print(list(netice))



