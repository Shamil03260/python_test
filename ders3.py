names = ["Nəsib", "Şamil", "Günel", "Ayan", "Nurlan"]


print("1. Ad əlavə etmək")
print("2. Ad silmək")
choice = int(input("Seçim edin: "))

if choice == 1:
    add_name = input("Ad daxil edin: ")
    names.append(add_name)
    print(names)
elif choice == 2:
    name = input("Ad daxil edin: ")
    if name == "":
        print("Error")
    else:
        if name not in names:
            print("Ad tapılmadı")
        else:
            names.remove(name)
            print(names)
else:
    print("Error")
