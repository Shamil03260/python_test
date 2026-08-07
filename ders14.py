#  sql

# import sqlite3

# conn = sqlite3.connect("school.db")

# cursor = conn.cursor()

# cursor.execute("""
               
#       CREATE TABLE IF NOT EXISTS students(
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           name VARCHAR(50),
#           age INTEGER
#       )        
               
#                """)


# cursor.execute(
#     "INSERT INTO students(name, age) VALUES (?, ?)",
#     ('Ayan',45)
# )

# cursor.execute("SELECT * FROM students ")

# print(cursor.fetchall())

# print(cursor.fetchone())

# print(cursor.fetchmany(5))


# cursor.execute("SELECT * FROM students WHERE age > 20 AND name = 'Fuad' ")

# cursor.execute("SELECT * FROM students WHERE age > 20 ORDER BY age DESC ")



# cursor.execute("SELECT * FROM students LIMIT 2,4 ")

# for age in cursor:
#     print(age)


# cursor.execute(
#     "UPDATE students SET age=? WHERE id=?",
#     (25, 1)
# )



# cursor.execute(
#     "UPDATE students SET id=15 WHERE id=2"
   
# )


# cursor.execute("DELETE FROM students WHERE id = 4 ")


# cursor.execute("DROP TABLE students")





# cursor.execute(
#     "INSERT INTO students(name, age) VALUES (?, ?)",
#     ('Ayan',45)
# )

# cursor.execute("SELECT COUNT(*) FROM students ")

# say = cursor.fetchone()[0]

# print(say)


# cursor.execute("SELECT DISTINCT name FROM students")

# cursor.execute("SELECT * FROM students WHERE name LIKE '%a' ")

# cursor.execute("SELECT * FROM students WHERE age IN (18,20)")


# cursor.execute("SELECT * FROM students WHERE age BETWEEN 18 AND 25")


# cursor.execute("""
               
               
# SELECT *
# FROM students
# WHERE NOT age = 18
 

# """)

# for i in cursor:
    
    
#     print(i)



# with sqlite3.connect("school.db") as conn:
#     cursor = conn.cursor()

#     cursor.execute(
#         "INSERT INTO students(name, age) VALUES (?, ?)",
#         ("Aysel", 21)
#     )
    
    

    
    
    
    
# sql task

import sqlite3
import random

win_or_lose = random.choice(["Qələbə", "Məğlubiyyət"])

conn = sqlite3.connect("casino.db")

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS casino(
    login TEXT PRIMARY KEY,
    password TEXT,
    cash INTEGER
)              
              
               """)


while True:
    print("---CASINO---")
    print("1. Qeydiyyatdan keçin")
    print("2. Oyuna başla")
    print("3. İstifadəçini bazadan silin")
    print("4. Balansı yoxlayın")
    print("5. Çıxış")
    
    choice = input("Seçiminizi edin: ")
    
    if choice == "1":
        
        login = input("Login: ")
        password = input("Password: ")
        cash = int(input("Balans: "))
        
        cursor.execute(
            "SELECT * FROM casino WHERE login=?",
            (login,)
        )
        
        existing_user = cursor.fetchone()
        
        if existing_user:
            print("Bu login artıq mövcuddur! Zəhmət olmasa başqa bir login seçin.")
            continue
        
        cursor.execute(
            "INSERT INTO casino(login, password, cash) VALUES (?, ?, ?)",
            (login, password, cash)
        )
        
        conn.commit()
        print("Qeydiyyat uğurla tamamlandı!")
        
    elif choice == "2":
        login = input("Login: ")
        password = input("Password: ")
        
        cursor.execute(
            "SELECT cash FROM casino WHERE login=? AND password=?",
            (login, password)
        )
        
        result = cursor.fetchone()
        
        if result:
            cash = result[0]
            print(f"Salam {login}! Sizin balansınız: {cash} AZN")
            
            outcome = random.choice(["Qələbə", "Məğlubiyyət"])
            
            if outcome == "Qələbə":
                cash += 10
                print(f"Təbriklər! Siz qazandınız! Yeni balansınız: {cash} AZN")
            else:
                cash -= 5
                print(f"Təəssüf! Siz uduzdunuz! Yeni balansınız: {cash} AZN")
            
            cursor.execute(
                "UPDATE casino SET cash=? WHERE login=?",
                (cash, login)
            )
            
            conn.commit()
        else:
            print("Yanlış login və ya şifrə!")
            
    elif choice == "3":
        login_to_delete = input("Silinəcək istifadəçinin loginini daxil edin: ")
        
        cursor.execute(
            "DELETE FROM casino WHERE login=?",
            (login_to_delete,)
        )
        
        conn.commit()
        print(f"{login_to_delete} adlı istifadəçi bazadan silindi!")
        
    elif choice == "4":
        login = input("Login: ")
        password = input("Password: ")
        
        cursor.execute(
            "SELECT cash FROM casino WHERE login=? AND password=?",
            (login, password)
        )
        
        result = cursor.fetchone()
        
        if result:
            cash = result[0]
            print(f"{login} adlı istifadəçinin balansı: {cash} AZN")
        else:
            print("Yanlış login və ya şifrə!")
            
    elif choice == "5":
        print("Çıxış edilir...")
        break
    
conn.close()