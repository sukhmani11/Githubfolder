import sqlite3
conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()
sql_query = """ CREATE TABLE book (
    
)"""