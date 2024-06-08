import sqlite3

conn = sqlite3.connect('db4.sqlite3')

create_table_query = """
CREATE TABLE IF NOT EXISTS "users" (
 id INT PRIMARY KEY,
 email VARCHAR(100) NOT NULL, 
 name VARCHAR(50), 
 birth_date DATETIME,
 is_admin INT DEFAULT 0
 )
"""

conn.execute(create_table_query)
conn.close()
