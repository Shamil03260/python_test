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



