# set() 
# unikal elementler qebul
# mutable
# index yoxdur



# my_set = {10, 2, 3, 3, 4 , 8 , 7, 8, -5}

# print(type(my_set))
# print(my_set)

# my_set.add(9)

# my_set.update([9, 10, 11])

# element yoxdursa xeta verir
# my_set.remove(0)

# element yoxdursa xeta vermir
# my_set.discard(0)

# my_set.pop()

# my_set.clear()


# my_set1 = {1, 2, 5}
# my_set2 = {3, 4, 1, 5}

# print(my_set1.union(my_set2))

# İzah: Ortaq elementləri qaytarır.
# a={1,2,3}
# b={2,3,4}
# print(a.intersection(b))


# İzah: Birinci set-də olub ikinci set-də olmayanları qaytarır.
# a={1,2,3}
# b={2,3}
# print(a.difference(b))





# print(my_set2)



# Dict və Set fərqləri
# Xüsusiyyət	Dict	Set
# Məlumat növü	Açar:Dəyər	Tək element
# Təkrarlanan element	Açar təkrarlanmır	Element təkrarlanmır
# Dəyər saxlayır	✅	❌
# Key var	✅	❌
# Ordered	✅ (Python 3.7+)	❌
# Mutable	✅	✅
# Hash Table	✅	✅
# İndeks	❌	❌
# Nested ola bilər	✅	Məhdud
# JSON-də istifadə	✅	❌
# API-lərdə istifadə	Çox	Az
# Django Model-lərdə	Çox	Nadir




# Dict/Set taskları

# task 1

my_dict = {
    "name": "Shamil",
    "age": 14,
    "city": "Baku",
    "is_student": True
}

print("1. Print keys")
print("2. Print values")

choice = input("Seçiminizi edin: ")

if choice == "1":
    print("Keys:")
    for key in my_dict.keys():
        print(key)
elif choice == "2":
    print("Values:")
    for value in my_dict.values():
        print(value)
else:
    print("Yanlış seçim")
    
    
# task 2

my_list = []
soz_sayi = {}

for word in range(10):
    user_input = input("söz daxil edin: ")
    my_list.append(user_input)

unique_words = set(my_list)
print("Təkrarlanmayan sözlər:", unique_words)
    
for word in my_list:
    if word in soz_sayi:
        soz_sayi[word] += 1
    else:
        soz_sayi[word] = 1

print("Sözların təkrarlanma sayı:", soz_sayi)


# task 3

products = {}

for i in range(5):
    product_name = input("Məhsul adı daxil edin: ")
    product_price = float(input("Məhsul qiymətini daxil edin: "))
    products[product_name] = product_price

search_product = input("Axtarış üçün məhsul adı daxil edin: ")

if search_product in products:
    print(f"{search_product}: {products[search_product]}")
else:
    print("Məhsul tapılmadı")
    

# task 4

students = {
"Ali":85,
"Veli":42,
"Murad":91,
"Aysel":58,
"Nigar":100
}

high_scorers = {}

for name, score in students.items():
    if score > 60:
        high_scorers[name] = score

print(f"60-dan böyük balı olan tələbələr: \n {high_scorers}")


# task 5

students = {
    "Ali": {"age": 20, 
            "city": "Baku", 
            "score": 85},
    
    "Veli": {"age": 22, 
             "city": "Ganja", 
             "score": 42},
    
    "Murad": {"age": 19, 
              "city": "Sumqayit", 
              "score": 91}
}



highest_score = max(students, key=lambda v: students[v]['score'])
print(f"Ən yüksək balı olan tələbə: {highest_score}")


# task 6

user1 = {"Ali","Murad","Samir","Aysel"}
user2 = {"Murad","Nigar","Ali","Leyla"}
common_friends = user1 & user2
print(f"Ortaq dostlar: {common_friends}")


# task 7

users = {
    "admin":"12345",
    "user":"11111",
    "guest":"22222"
}

login = input("İstifadəçi adını daxil edin: ")
password = input("Parolu daxil edin: ")

if login in users.keys() and users[login] == password:
    print("Xoş gəldiniz")
else:
    print("İstifadəçi adı və ya parol yanlışdır.")