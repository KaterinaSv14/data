import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()

cursor.execute(
    "create table if not exists movies "
    "(id integer primary key, title string, director string, year integer, genre string);"
)
connection.commit()

cursor.execute(
    "insert into movies (title, director, year, genre) values ('Film1', 'Director1', 2024, 'Fiction');"
)
cursor.execute(
    "insert into movies (title, director, year, genre) values ('Film2', 'Director2', 2023, 'Fiction');"
)
cursor.execute(
    "insert into movies (title, director, year, genre) values ('Film3', 'Director3', 2022, 'Fiction');"
)
cursor.execute(
    "insert into movies (title, director, year, genre) values ('Film4', 'Director4', 2021, 'Fiction');"
)
cursor.execute(
    "insert into movies (title, director, year, genre) values ('Film5', 'Director5', 2020, 'Fiction');"
)
connection.commit()

name = 'Director5'
cursor.execute(
    f"select * from movies where director = '{name}';"
)
print(name)
for director in cursor.fetchall():
    print(director)
connection.commit()

year = 2019
title = 'Film5'
cursor.execute(
    f"update movies set year = {year} where title = '{title}';"
)
connection.commit()

delete = 'Film3'
cursor.execute(
    f"delete from movies where title = '{delete}';"
)
connection.commit()

connection.close()
