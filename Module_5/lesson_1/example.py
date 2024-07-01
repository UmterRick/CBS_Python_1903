# sync: psycopg2 / psycopg2-binary
# async analog: asyncpg

import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM books")

result = cursor.fetchmany(size=3)
print(result)
print()
for book in result:
    print(book)