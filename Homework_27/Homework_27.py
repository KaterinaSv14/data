import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()

cursor.execute(
    "create table if not exists books (id integer primary key, title text, author text, year integer, genre text);"
)
connection.commit()

cursor.execute(
    "insert into books (title, author, year, genre) values ('Book1', 'Author1', 2024, 'Fiction');"
)
cursor.execute(
    "insert into books (title, author, year, genre) values ('Book2', 'Author2', 2023, 'Fiction');"
)
cursor.execute(
    "insert into books (title, author, year, genre) values ('Book3', 'Author3', 2022, 'Fiction');"
)
cursor.execute(
    "insert into books (title, author, year, genre) values ('Book4', 'Author4', 2021, 'Fiction');"
)
cursor.execute(
    "insert into books (title, author, year, genre) values ('Book5', 'Author5', 2020, 'Fiction');"
)
connection.commit()

name = 'Author1'
cursor.execute(
    f"select * from books where author = '{name}';"
)
print(f'Books autor {name}:')
for author in cursor.fetchall():
    print(author)
connection.commit()

year = 2019
title = 'Book5'
cursor.execute(
    f"update books set year = {year} where title = '{title}';"
)
connection.commit()

delete = 'Book3'
cursor.execute(
    f"delete from books where title = '{delete}';"
)
connection.commit()

connection.close()
