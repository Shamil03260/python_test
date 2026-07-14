# # number = 5

# # if number > 10:
# #     print("Şərt ödəndi")
    
# # elif number > 5:
# #     print("ədəd 5-dən böyükdür")
    
# # else:
# #     print("Heç bir şərt ödənmir")
    
    
# # age = 20

# # if age > 18:
# #     print("Yetkin")
# # else:
# #     print("Yetkin deyil")


# # name = "Shamil"

# # if "n" in name:
# #     print("Şərt ödənir")
# # else:
# #     print("Şərt ödənmir")
    
    
# # city = "Baku"

# # if "z" not in city:
# #     print("Şərt ödənir")
# # else:
# #     print("Şərt ödənmir")


# # city = "London"

# # if "r" in city or "b" in city or "a" in city:
# #     print("Şərt ödənir")
    
# # else:
# #     print("Şərt ödənmir")
    
    
# # name = "Ayan"

# # if "z" in name and "a" in name:
# #     print("Şərt ödənir")
    
# # else:
# #     print("Şərt ödənmir")


# # number = int(input("Enter the number: "))

# # if number > 0:
# #     print("positive")

# # elif number < 0:
# #     print("Negative")

# # else:
# #     print("Zero")


# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))

# # print("Maksimum ədəd: ", max(num1, num2))
# # print("Minimum ədəd: ", min(num1, num2))


# # num1 = int(input("Enter the first number: "))
# # num2 = int(input("Enter the second number: "))

# # print(pow(num1, num2)) 



# if elif else taskları

# task 1

age = int(input("Yaşınızı dsaxil edin: "))

if age > 18:
    print("Giriş icazəlidir")
else:
    print("Giriş qadağandır")


# task 2

num1 = 34
num2 = 65


max_numbers = max(num1, num2)

print(f"Maksimum ədəd: {max_numbers}")



# task 3

score = 30

if score >= 91:
    print("A")
elif score >= 71:
    print("B")
elif score >= 51:
    print("C")
elif score >= 31:
    print("C")
else:
    print("F")
    

# task 4

number = 5

if number > 0:
    print("Ədəd müsbətdir")
elif number < 0:
    print("Ədəd mənfidir")
else:
    print("Ədəd sıfırdır")
    

# task 5

month_digit = 7

if month_digit == 12 or month_digit == 1 or month_digit == 2:
    print("Qış")
elif month_digit == 3 or month_digit == 4 or month_digit == 5:
    print("Yaz")
elif month_digit == 6 or month_digit == 7 or month_digit == 8:
    print("Yay")
elif month_digit == 9 or month_digit == 10 or month_digit == 11:
    print("Payız")
    

# task 6

username = input("İstifadəçi adı: ").capitalize
password = input("Şifrə: ")

correct_username = "Şamil"
correct_password = "1212"

if username == correct_username and password == correct_password:
    print("Giriş uğurludur")
else:
    print("İstifadəçi adı və ya şifrə yanlışdır")
    

# task 7

number = 86

if number % 2 == 0:
    print("Bu ədəd cütdür")
else:
    print("Bu ədəd təkdir")


# task 8

num1 = 54
num2 = 76
num3 = 25

num_max = max(num1, num2, num3)

print(f"Maksimum ədəd: {num_max}")


# task 9

login = input("Login: ")
password = input("Parol: ")

correct_login = "nasib"
correct_password = "12345"

if login == "" and password == "":
    print("Login ve parol daxil etmediniz")

elif login == "":
    print("Login daxil etmediniz")

elif password == "":
    print("Parol daxil etmediniz")

elif login != correct_login and password != correct_password:
    print("Login ve parol yanlishdir")

elif login != correct_login:
    print("Login yanlishdir")

elif password != correct_password:
    print("Parol yanlishdir")

else:
    print("Xosh geldiniz Nasib")
    

# task 10

name = input("Ad daxil edin: ").capitalize

if name == "Aslan":
    print("Aslan emi ogludur") 
elif name == "Imran":
    print("Imran dayi ogludur")
elif name == "Afaq":
    print("Afaq bibi qizidir")
elif name == "Uzeyir":
    print("Uzeyir xala ogludur")
elif name == "Shahin":
    print("Shahin yaxin dostdur")
else:
    print(f"{name} kimdir? Mən onu tanımıram")
    

# task 11

height = float(input("Boyunuzu daxil edin (m): "))
weight = float(input("Kütlənizi daxil edin (kg): "))

bki = weight / (height * height)

if bki < 18.5:
    print("Zəif")
elif bki < 25:
    print("Normal")
elif bki < 30:
    print("Kilolu")
else:
    print("Obez")