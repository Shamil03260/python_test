# list comprehension



# my_list = [1, 2, 3, 4, 5]

# for i in my_list:
#     if i % 2 == 0:
        
#         print("success")

  
# result=[]
# for x in range(1,6):
#     result.append(x*x)


# kvadratlar = [x*x for x in range(1,6)]

# my_list = [i for i in range(1,10) if i % 2 == 0 ]

# print(my_list)


# result={}

# for x in range(1,6):
#     result[x]=x*x
    
# print(result)


# kvadratlar = {x: x*x for x in range(1,6)}
# print(kvadratlar)



# text = input("Mətn daxil et: ")
# c = int(input("Sayını daxil et: "))
# i = 0

# while i != c:
#     i += 1
#     print(f"{i}. {text}")



# for / while taskları

# task 1

sum_list = []
c_num = int(input("Neçə ədəd daxil edəcəksiniz?: "))

for _ in range(c_num):
    while True:
        num = int(input("Ədəd daxil et: "))
        if num >= 0:
            sum_list.append(num)
            break
        else:
            print("Müsbət ədəd daxil edin!")

print("Cəm:", sum(sum_list))


# task 2

balance = 0
history = []

while True:
    print("===== MENYU =====")
    print("1. Balans")
    print("2. Pul əlavə et")
    print("3. Pul çıxar")
    print("4. Tarixçə")
    print("5. Çıxış")
    
    choice = input("Seçiminizi edin: ")
    
    if choice == "1":
        print(f"Balans: {balance} AZN")
    
    elif choice == "2":
        amount = int(input("Əlavə etmək istədiyiniz məbləği daxil edin: "))
        if amount > 0:
            balance += amount
            history.append(f"{amount} AZN balansa əlavə edildi")
            print(f"{amount} AZN balansınıza əlavə edildi")
        else:
            print("Müsbət bir məbləğ daxil edin!")
            
    elif choice == "3":
        amount = int(input("Çıxarmaq istədiyiniz məbləği daxil edin: "))
        if amount <= balance:
            balance -= amount
            history.append(f"{amount} AZN balansınızdan çıxarıldı")
            print(f"{amount} AZN balansınızdan çıxarıldı")
        else:
            print("Balansınız o qədər vəsait yoxdur və ya mənfi məbləğ daxil etdiniz!")
            
    elif choice == "4":
        print("===== TARİXÇƏ =====")
        for h in history:
            print(h)
            
    elif choice == "5":
        print("Çıxış edilir...")
        break
    

# task 3

grades = []

c_students = int(input("Neçə şagird var?: "))

for ad in range(c_students):
    name = input("Şagirdin adını daxil et: ")
    
    
    for i in range(3):
        while True:
            grade = int(input(f"{name} üçün {i + 1}. qiyməti daxil et (0-100): "))
            if 0 <= grade <= 100:
                grades.append(grade)
                break
            else:
                print("Qiymət 0–100 arasında olmalıdır. Yenidən daxil edin.")
    
    average = sum(grades) / len(grades)
    
    if average >= 50:
        status = "Keçdi"
    else:
        status = "Kəsildi"
        
    print(f"{name} üçün orta bal: {average}. Status: {status}")
    
    
# task 4

numbers = []

for i in range(10):
    num = int(input("Ədəd daxil et: "))
    numbers.append(num)
    
print("Ədədlərin cəmi:", sum(numbers))


# task 5

for i in range(6):
    word = input("söz daxil et: ")
    print(f"{word} -> {len(word)}")
    
    
# task 6

for i in range(5):
    word = input("Söz daxil et: ")
    
    if word.startswith("a"):
        print(f"{word} 'a' hərfi ilə başlayır.")
        
    if word.endswith("a"):
        print(f"{word} 'a' hərfi ilə bitir.")
        
    if len(word) > 5:
        print(f"{word} uzunluğu 5-dən böyükdür.")
        

# task 7

words = []

for i in range(5):
    word = input("Söz daxil et: ").upper()
    words.append(word)
    
print("Daxil edilmiş sözlər:", words)