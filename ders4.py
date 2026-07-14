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



# list/tuple taskları

# task 1

num1 = int(input("Birinci ədədi daxil edin: "))
num2 = int(input("İkinci ədədi daxil edin: "))
num3 = int(input("Üçüncü ədədi daxil edin: "))

numbers = []

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)

numbers.sort()
print(f"Artan sıra: {numbers}")

max_in_list = max(numbers)
min_in_list = min(numbers)

numbers.remove(max_in_list)
numbers.remove(min_in_list)

print(f"Əb böyük və ən kiçik ədədlər silindi: {numbers}")

numbers = tuple(numbers)
print(f"Tuple: {numbers}")


# task 2

numbers = [5, 8, 2, 1, 5, 9, 2, 6, 1, 8]
unique_numbers = set(numbers)
numbers = list(unique_numbers)
print(f"Yalnız unikal ədədlər: {numbers}")

numbers.sort()
numbers = tuple(numbers)
print(f"Artan sıra: {numbers}")


# task 3

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

list3 = list1 + list2
  
print(f"Birləşdirilmiş list: {list3}")

del list3[0:3]

del list[-2:-1]

print(f"List yeniləndi: {list3}")


# task 4

names = []

while True:
    name = input("Ad daxil edin: ")

    if name == "stop":
        break

    names.append(name)

names = set(names)
len_names = len(names)
print(f"Unikal adlar: {names}")
print(f"Unikal adların sayı: {len_names}")


# task 5

list = [12, 4, 8, 15, 20, 7, 10, 5]

cut = []
tek = []

for x in list:
    if x % 2 == 0:
        cut.append(x)
    else:
        tek.append(x)

print(f"Cüt ədədlər: {cut}")
print(f"Tək ədədlər: {tek}")


# Task 6

numbers = []
numbers.append(5)
numbers.append(8)
numbers.append(2)
numbers.append(1)
numbers.append(6)
numbers.append(11)
numbers.append(23)
numbers.append(54)
numbers.append(3)
numbers.append(16)

maximum = max(numbers)
minimum = min(numbers)

print(f"Ən böyük ədəd: {maximum}")
print(f"Ən kiçik ədəd: {minimum}")

sum = sum(numbers)
average = sum / len(numbers)
print(f"Orta qiymət: {average}")

cut = []
tek = []

for x in numbers:
    if x % 2 == 0:
        cut.append(x)
    else:
        tek.append(x)
        
len_cut = len(cut)
len_tek = len(tek)

print(f"Cüt ədədlərin sayı: {len_cut}")
print(f"Tək ədədlərin sayı: {len_tek}")


# Task 7

tuple1 = (1, 2, 3, 4)
tuple2 = (5, 6, 7, 8)

tuple1 = list(tuple1)
tuple2 = list(tuple2)

combined_list = tuple1 + tuple2
combined_list.sort()

tuple3 = tuple(combined_list)


# Task 8

numbers = list(range(1, 101))


for number in numbers:
    if number % 3 == 0:
        numbers.remove(number)
        
numbers_divisible_by_5 = []

for number in numbers:
    if number % 5 == 0:
        numbers.remove(number)
        numbers_divisible_by_5.append(number)

numbers = tuple(numbers)
numbers_divisible_by_5 = tuple(numbers_divisible_by_5)

print()

# Task 9

mixed_list = [1, 2.5, "hello", True, 3, 4.7, "world", False, 5]
list_of_integers = []

for item in mixed_list:
    if type(item) == int:
        list_of_integers.append(item)

print(f"Integer-lər: {list_of_integers}")