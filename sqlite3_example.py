#Sample program to demonstrate sqlite3 library. This program will perform basic SQL operations of
#create a table, insert, update, delete and select.

import sqlite3

def create_table():
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store( item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(item, quantity, price):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(?,?,?)",(item, quantity, price))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(item):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("DELETE FROM store where item = ?",(item,))
	conn.commit()
	conn.close()

def update(quantity, price, item):
	conn = sqlite3.connect('lite.db')
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?",(quantity, price, item))
	conn.commit()
	conn.close()

# create_table()
# insert('Coffee glass', 10, 200.3)
# insert('Water Glass', 5, 100)
# insert('Beer Glass', 20, 5000)
#delete('Beer Glass')
#update(10, 1500, 'Water Glass')
print(view())

