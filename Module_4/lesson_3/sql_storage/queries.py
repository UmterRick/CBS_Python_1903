import sqlite3

"""
SQL - Structured Query Language
CRUD - Create Read Update Delete
"""

conn = sqlite3.connect('db.sqlite3')

conn.execute('CREATE TABLE IF NOT EXISTS "movies" (id, title, director, release_year)')

data = conn.execute('SELECT * FROM movies')
fetched_data = data.fetchall()
print(data)
print(fetched_data)
#
# conn.execute(
#     """
#     INSERT INTO movies(id, title, director, release_year) VALUES (1, "Avatar", "Cameron", 2009)
#     """
# )
# conn.commit()
#
# conn.execute(
#     """
#     INSERT INTO movies(id, title, director, release_year) VALUES
#     (2, "Avatar 2", "Cameron", 2023),
#     (3, "Terminator", "Cameron", 1000),
#     (4, "Terminator 2", "Cameron", 1002);
#     """
# )
# conn.commit()


data = conn.execute('SELECT * FROM movies').fetchall()
print(data)
print()
sql_query = "SELECT title, release_year FROM movies WHERE director='Cameron' OR release_year>2000"
data = conn.execute(sql_query).fetchall()
print(data)


sql_query = "UPDATE movies SET director='Cameron' WHERE id=1"
conn.execute(sql_query)
conn.commit()


sql_query = "DELETE FROM movies WHERE id=3"
conn.execute(sql_query)
conn.commit()
