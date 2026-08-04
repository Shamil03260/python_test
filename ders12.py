#  txt fayllar
# with - context manager

# my_file = open("baza.txt","r")


# my_file = open("baza.txt","w")

# my_file.write("test")

# my_file = open("baza.txt","a")

# my_file.write("Go PHP")


# my_file = open("baza.txt","r")

# print(my_file.read())


# with open("baza.txt") as file:
    
#     print(file.read())




# with open("baza.txt") as file:
#     print(file.readline())
#     print(file.readline())


# with open("baza.txt") as file:
#     data = file.readlines(3)

# print(data)

# students = [
#     "Əli\n",
#     "Ömər\n",
#     "Ilqar\n",
#     "ı"
    
    
# ]



# with open("baza.txt","w",encoding="utf-8") as file:
#     file.writelines(students)


# with open("baza.txt") as file:
#     for line in file:
#         print(line.strip())




# while True:
#     ad = input("Ad daxil edin (bitirmək üçün stop): ")

#     if ad.lower() == "stop":
#         break

#     with open("baza.txt", "a", encoding="utf-8") as file:
#         file.write(ad + "\n")
        
        
        
# with open("baza.txt", "r", encoding="utf-8") as file:
#     for ad in file:
#         print(ad.strip())

# import pandas as pd

# df = pd.read_csv("baza.txt", header=None)

# df.to_excel("students.xlsx", index=False)
