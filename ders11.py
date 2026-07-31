# import math
# from math import sqrt

# math.sqrt

# print(sqrt(16))




# import math

# print(math.sqrt(49))
# print(math.pi)
# print(math.factorial(5))

# print(math.ceil(4.1))
# print(math.floor(4.9))



# import random

# print(random.randint(1, 9999))

# meyveler = ["alma", "armud", "banan"]

# print(random.choice(meyveler))

# random.shuffle(meyveler)

# print(meyveler)


# from datetime import datetime

# import datetime

# indiki = datetime.now()

# print(indiki)

# print(datetime.timedelta(days=1))

# print(indiki.strftime("%Y"))

# import time


# time.sleep(3)
# print("bashladi")



# import os

# print(os.getcwd())

# os.makedirs("test1")

# os.remove("test3.txt")

# os.rmdir("test5")





# import sys

# print(sys.version)



# import statistics

# ededler = [10,20,30,40]

# print(statistics.mean(ededler))



# import string

# print(string.ascii_lowercase)

# print(string.digits)


# import json


# user = {
#     "name": "Ali",
#     "age": 20
# }

# Dictionary-ni JSON String-ə çevirir.
# json_data = json.dumps(user)

# print(type(json_data))


# print(type(user))


# import json

# text = '{"name":"Ali","age":22}'
# JSON String-i yenidən Dictionary-yə çevirir.
# user = json.loads(text)

# print(type(user))


# user = {
#     "name": "Ali",
#     "age": 20
# }

# print(json.dumps(user, indent=4))



# user = {
#     "ad": "Əli"
# }


# print(json.dumps(user, ensure_ascii=False, indent=4))

# import requests

# response = requests.get("https://oxu.az")

# print(response.content)


# from pathlib import Path

# fayl = Path("ders1.py")

# print(fayl.exists())


# import re

# text = "Mən Python öyrənirəm."

# netice = re.search("Python", text)

# print(netice)



# import re

# text = "alma armud alma banan alma"

# print(re.findall("alma", text))



# import re

# text = "alma,armud,banan"

# print(re.split(",", text))


# import re

# text = "Salam Əli"

# print(re.sub("Əli", "Vəli", text))


# import re

# print(re.findall("a.", "alma ata ana"))



# import re

# text = "Yaşım 25-dir."


# print(re.findall(r"\d", text))


# import re

# print(re.findall(r"\D", "A1B2"))



# import re

# print(re.findall(r"\w", "Ali_25"))


# import re

# print(re.findall(r"\W", "Ali@25"))


# import re

# text = "Python çox gözəldir."

# print(re.search("^Python", text))



# import re

# text = "Salam"

# print(re.search("Salam$", text))




# Libraries taskları

# task 1

import datetime

birth_year = int(input("Doğulduğunuz il: "))
birth_month = int(input("Doğum ayınız: "))
birth_day = int(input("Doğum gününüz: "))

birth_date = datetime.datetime(birth_year, birth_month, birth_day)
current_date = datetime.datetime.now()

age = current_date - birth_date

seconds = age.total_seconds()
minutes = seconds // 60
hours = minutes // 60
days = hours // 24

print(f"Siz həyatda {int(seconds)} saniyə, {int(minutes)} dəqiqə, {int(hours)} saat, {int(days)} gündür ki mövcudsunuz və sizin {int(current_date.year - birth_year)} yaşınız var")


# task 2

import re

text = """
Əlaqə: 
ali@gmail.com
veli@yahoo.com
test@test.az
"""


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'


emails = re.findall(email_pattern, text)

print(emails)


# task 3

text = """
Ali 20 yaşındadır.
Vəli 18 yaşındadır.
Murad 25 yaşındadır.
"""

numbers = re.findall(r'\d+', text)
print(numbers)


# task 4

password = input("Şifrəni daxil edin: ")

if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$', password):
    print("Şifrə düzgündür.")
else:
    print("Şifrə uyğun deyil.")
    
    
# task 5

name = input("Adınızı daxil edin: ")
birth_date = input("Doğum gününüzü daxil edin (gün.ay.il): ")
birth_date = datetime.datetime.strptime(birth_date, "%d.%m.%Y")
current_date = datetime.datetime.now()
remaining_time = birth_date - current_date

print(f"Hörmətli {name}, sizin ad gününüzə {birth_date} tarixində {remaining_time.days} gün, {remaining_time.seconds // 3600} saat, {(remaining_time.seconds % 3600) // 60} dəqiqə, {remaining_time.seconds % 60} saniyə qalıb.")