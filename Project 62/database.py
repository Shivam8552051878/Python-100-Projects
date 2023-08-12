import sqlite3


db = sqlite3.connect("books-collection.db")

cursor = db.cursor()
# cursor.execute('CREATE TABLE books '
#                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title varchar(250) NOT NULL UNIQUE, '
#                'author varchar(250) NOT NULL, rating FLOAT NOT NULL)')


# cursor.execute("INSERT INTO books VALUES('4',' Potter', 'J. K. Rowling', '9.5')")
print(cursor.execute("SELECT * FROM books").fetchall())
db.commit()
db.close()