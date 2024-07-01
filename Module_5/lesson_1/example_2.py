import psycopg2

from Module_5.lesson_1.const import CONNECTION_PARAMS

conn = psycopg2.connect(**CONNECTION_PARAMS)

create_book_table = """
    CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    published_date DATE
    );
"""


create_author_table = """
    CREATE TABLE IF NOT EXISTS authors (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        birth_date DATE
    );
"""


create_books_authors_table = """
    CREATE TABLE IF NOT EXISTS books_authors (
        book_id INT NOT NULL,
        author_id INT NOT NULL,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id) REFERENCES books (id) ON DELETE CASCADE, 
        FOREIGN KEY (author_id) REFERENCES authors (id) ON DELETE CASCADE 
    );
"""

cursor = conn.cursor()
cursor.execute(create_book_table)
cursor.execute(create_author_table)
cursor.execute(create_books_authors_table)

conn.commit()

cursor.close()
conn.close()