#  for while

# nums = [1, 2 ,3]

# it = iter(nums)

# print(next(it))
# print(next(it))
# print(next(it))

# print(" --- ")

# for x in [1,2,3]:
#     print(x)


# range(start, stop, step) ardıcıllıq yaradır.
# for i in range(1, 10, 3):
#     print(i)

# language = "English"

# language = (1, 2, 3)

# language = {"lang":"Python", "lang2":"php"}

# for i in language.items():
#     print(i)


# i=0

# while i<5:
#     i+=1
#     print(i)
    
# while True:
#     print("----")
    
    
# 5 x 1 = 10
# 5 x 2
# 5 x 3
# 5 x 4
    
    
# i = 0

# number = int(input("Eded daxil edin : "))

# if number == 0 or  number > 10:
#     print("error")
# else:
#     while i < 10:
#         # i = i +1 
#         i += 1
        
#         answer = number * i
#         print(number,"x", i, "=",answer )



# for i in range(10):
#     if i==5:
#         break
#     print(i)

    
# i = 0

# while i < 5:
#     i += 1
#     if i == 3:
#         break
#     print(i)



# for i in range(6):
#     if i==3:
#         continue
#     print(i)



# for i in range(3):
 
#     print(i)
# else:
#     print("Bitdi")
    



# password='1234'
# user=''
# while user!=password:
#     user=input('Parol: ')
    
# print('Xoş gəldiniz')



# adlar=["Ali","Vəli","Aysel"]


    
# for index, name in enumerate(adlar,start=1):
#     print(index, name)

# 0 - Ali
# 1 - Veli

# adlar=["Ali", "Vəli", "Akif"]

# ballar=[90, 80, 50]

# for ad,bal in zip(adlar,ballar):
#     print(ad,bal)


# for x in reversed([10,20,30]):
#     print(x)



# i = 0

# number = int(input("Number: "))
# if number > 10 or number == 0:
#     print("Error")
    
# else:
#     while i < 10:
#         i += 1
#         answer = number * i 
#         print(number, "x", i, "=", answer)

# row = 1

# while row <= 10:
#     col = 1
#     while col <= 10:
#         result = row * col
#         print(f"{row} x {col} = {result}", end="\t")
#         col += 1
#     print()  
#     row += 1