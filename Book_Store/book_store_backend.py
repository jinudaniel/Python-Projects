import sqlite3

def connect():
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
	conn.commit()
	conn.close()

connect()

def insert(title, author, year, isbn):
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO book VALUES(NULL, ?,?,?,?)", (title, author, year, isbn))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM book")
	rows = cur.fetchall()
	conn.close()
	return rows

def search(title = "", author="", year="", isbn=""):
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM book where title = ? OR author = ? OR year = ? OR isbn = ?",(title, author, year, isbn))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM book where id = ?", (id,))
	conn.commit()
	conn.close()

def update(id, title, author, year, isbn):
	conn = sqlite3.connect('books.db')
	cur = conn.cursor()
	cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))
	conn.commit()
	conn.close()

#insert("Kite Runner", "Khaled", 1980, 9563946)
#insert("The earth", "Jinu Daniel", 1920, 9564525)
#insert("The Sun", "Deepshikha", 1990, 9930126)
#delete(1)
#update(3, "The Sun", "Deepshikha Arora", 1990, 9930126)
print(search(author="Deepshikha Arora"))
print(view())	

