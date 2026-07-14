#  tuple()
#  immutable
#  tekrar elementler qebul edir
#  tuple listden suretlidi


# number = (1, 2, 3, 4, 5, 4)

# print(type(number))

# print(number[0])

# print(number.index(1))

# print(number.count(4))



#  python memory management 

# import sys 

# number1 = (1, 2, 3)
# number2 = [1, 2, 3]

# print("tuple ucun yaddas", sys.getsizeof(number1))
# print("list ucun yaddas", sys.getsizeof(number2))


# number = (1, 2, [1, 2])

# print(type(number))

# print(type(number[2]))


# number[2].append(3)

# print(number)



# my_list = ["apple", "cherry", "orange", "banana"]

# last_value = my_list[-1]

# if last_value.startswith("b"):
#     print("True")
# else:
#     print("False")