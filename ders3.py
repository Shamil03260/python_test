# listler list()
#  mutable
#  tekrar elementler qebul edir

# some_list = []

# print(type(some_list))


# some_list = ["Python", "Go", "Java", "PHP", 6, 2.5, True]


# some_list.append(4) sona element elave edir

# some_list.insert(2,4) indekse gore element elave etmey

# some_list.remove("Go") deyere gore elementi silir


# some_list.pop(1) default olaraq sonuncunu silir , indeks yazsaq indekse gore silir


# some_list.pop(2)

# some_list.clear() bosh list qaytarir


# print(some_list[0]) 

# print(some_list.index(3))

# print(some_list)



# some_list = [1, 2, 3, 2, 2, 5, 7 ,7]

# print(some_list.count(7)) elementleri sayir



# some_list.sort() sira ile cesidleyir 



# some_list.sort()

# some_list.reverse() listi tersine yazdirir

# b = some_list.copy() listi copy edir

# print(id(some_list))
# print(id(b))

# print(b)
# print(some_list)



# some_list = [5, 6, 0, 10, 66, 3]

# some_list.sort()

# some_list.reverse()

# print(some_list)


# names = ["Nəsib", "Şamil", "Günel", "Ayan", "Nurlan"]


# print("1. Ad əlavə etmək")
# print("2. Ad silmək")
# choice = int(input("Seçim edin: "))

# if choice == 1:
#     add_name = input("Ad daxil edin: ")
#     names.append(add_name)
#     print(names)
# elif choice == 2:
#     name = input("Ad daxil edin: ")
#     if name == "":
#         print("Error")
#     else:
#         if name not in names:
#             print("Ad tapılmadı")
#         else:
#             names.remove(name)
#             print(names)
# else:
#     print("Error")