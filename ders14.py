import sqlite3

conn = sqlite3.connect("school.db")

c = conn.cursor()

c.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
               """)


# c.execute("INSERT INTO Students VALUES(NULL, 'Ali')")
# conn.commit()

# c.execute(
#     "INSERT INTO students(name) VALUES(?)",
#         ('Shamil',)
# )
# conn.commit()

c.execute("SELECT * FROM students")

# print(c.fetchall())
# print(c.fetchone())
# print(c.fetchmany(2))


# c.execute(
#     "INSERT INTO students(name, age) VALUES(?, ?)",
#         ('Ali', 17)
#         ('Shamil', 14)
#         ('Aylin', 20)
# )

# conn.commit()


# c.execute("SELECT * FROM students WHERE age < 18")


# c.execute("SELECT * FROM students WHERE age < 18 ORDER BY age")

# c.execute("SELECT * FROM students LIMIT 2,4")

# c.execute("UPDATE students SET age = 22 WHERE id = 3")
# conn.commit()

# c.execute(
#     "UPDATE students SET age = ? WHERE id = ?",
#         (23, 3)
    
#           )

# conn.commit()


for age in c:
    print(age)
    
    