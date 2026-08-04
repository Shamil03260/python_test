# try:
    
#     print(10/0)
#     print("her sey qaydasindadi")

# except ZeroDivisionError:
#     print("0 -a bolmey olmaz")
    



# try:
    
#     print("Başladı")

#     a = 10

#     print(a/0)

#     print("Bitdi")

# except:
#     print("Xəta tutuldu.")



# try:
#     a = int(input())

#     print(10/a)

# except ValueError:
#     print("Rəqəm daxil edin.")

# except ZeroDivisionError:
#     print("0 olmaz.")


# try:
#     print(10/0)

# except ZeroDivisionError as e:
#     print(e)



# try:
#     print(10/0)

# except ZeroDivisionError:
#     print("Problem.")

# else:
#     print("Hər şey qaydasındadır.")




# try:
#     print(10/0)

# except Exception as e:
#     print(type(e))
# finally:
#     print("her shey oz qaydasinadir")


# yas = -5

# if yas < 0:
#     raise ValueError("Yaş mənfi ola bilməz.")


# try:
#     yas = int(input("Yaş: "))

#     if yas < 0:
#         raise ValueError("Yaş mənfi ola bilməz.")

#     print("Yaş:", yas)

# except ValueError as e:
#     print("Xəta:", e)


# import requests

# try:

#     response = requests.get("https://oxasdasdu.az", timeout=5)
#     print(response.status_code)

# except requests.exceptions.RequestException as e:
#     print("Sorğu zamanı problem baş verdi.")
#     print(e)







# Python txt files və try except taskları

# task 1

with open("qiymetler.txt", "r") as file:
    try:
        qiymetler = []
        for qiymet in file:
            qiymet = int(qiymet.strip())
            qiymetler.append(qiymet)
        ortalama = sum(qiymetler) / len(qiymetler)
        print("Ortalama:", ortalama)
    except ValueError:
        print("Faylda düzgün olmayan qiymət var.")
    except ZeroDivisionError:
        print("Fayl boşdur, ortalama hesablamaq mümkün deyil.")
        
        
# task 2

file_name = input("Fayl adı daxil edin: ")

try:
    with open(file_name, "r") as file:
        content = file.read()
        
    with open("copy.txt", "w") as copy_file:
        copy_file.write(content)
        
    print(f"{file_name} faylı copy.txt faylına kopyalandı.")
    
except FileNotFoundError:
    print("Belə fayl tapılmadı.")
    
    
# task 3

try:
    with open("cumleler.txt", "r") as file:
        lines = file.readlines()
    
    if not lines:
        print("Fayl boşdur.")
    else:
        longest_line = max(lines, key=len)
        print("Ən uzun sətr:", longest_line.strip())
        print("Simvol sayı:", len(longest_line.strip()))

except FileNotFoundError:
    print("Fayl tapılmadı.")
    
    
# task 4

try:
    with open("numbers.txt", "r") as file:
        total = 0
        for line in file:
            line = line.strip()
            try:
                number = int(line)
                total += number
            except ValueError:
                print(f"{line} keçildi")
    
    print("Cəmi:", total)
except FileNotFoundError:
    print("Fayl tapılmadı.")
    

# task 5

try:
    with open("adlar.txt", "r") as file:
        adlar = set()
        for ad in file:
            ad = ad.strip()
            adlar.add(ad)
    
    with open("unique.txt", "w") as unique_file:
        for ad in sorted(adlar):
            unique_file.write(ad + "\n")
    
    print("Təkrarlanmayan adlar unique.txt faylına yazıldı.")
    
except FileNotFoundError:
    print("Fayl tapılmadı.")
    

# task 6

meyveler = ["alma", "armud", "banan"]

try:
    indeks = int(input("İndeks daxil edin: "))
    print("Seçilmiş meyvə:", meyveler[indeks])
except IndexError:
    print("Belə indeks yoxdur.")
    

# task 7

import random

number = random.randint(1, 100)

while True:
    guess = input("1-100 arası rəqəm daxil edin (çıxmaq üçün 'exit'): ")

    try:
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Zəhmət olmasa 1-100 arası rəqəm daxil edin.")
            continue

        if guess < number:
            print("Daha böyük bir rəqəm daxil edin.")
        elif guess > number:
            print("Daha kiçik bir rəqəm daxil edin.")
        else:
            print("Təbriklər! Düzgün tapdınız:", number)
            break

    except ValueError:
        print("Zəhmət olmasa düzgün bir rəqəm daxil edin.")
        

# task 8

username = input("İstifadəçi adı: ")
password = input("Şifrə: ")

if not username or not password:
    print("İstifadəçi adı və ya şifrə boş ola bilməz.")
else:
    print("Giriş uğurla tamamlandı.")