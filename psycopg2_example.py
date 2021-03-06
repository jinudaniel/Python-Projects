#Sample program to demonstrate psycopg2 library. This program will perform basic SQL operations of
#create a table, insert, update, delete and select on Postgre SQL database. Inorder to run this program
#PostgreSQL should be installed in your local computer

import psycopg2

def create_table():
	#Enter the password for your postgresql in the password attribute
	conn = psycopg2.connect("dbname = 'Database1' user='postgres' password='' host = 'localhost' port = '5432'")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS store( item TEXT, quantity INTEGER, price REAL)")
	conn.commit()
	conn.close()

def insert(item, quantity, price):
	#Enter the password for your postgresql in the password attribute
	conn = psycopg2.connect("dbname = 'Database1' user='postgres' password='' host = 'localhost' port = '5432'")
	cur = conn.cursor()
	cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
	conn.commit()
	conn.close()

def view():
	#Enter the password for your postgresql in the password attribute
	conn = psycopg2.connect("dbname = 'Database1' user='postgres' password='' host = 'localhost' port = '5432'")
	cur = conn.cursor()
	cur.execute("SELECT * FROM store")
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(item):
	#Enter the password for your postgresql in the password attribute
	conn = psycopg2.connect("dbname = 'Database1' user='postgres' password='' host = 'localhost' port = '5432'")
	cur = conn.cursor()
	cur.execute("DELETE FROM store where item = %s",(item,))
	conn.commit()
	conn.close()

def update(quantity, price, item):
	#Enter the password for your postgresql in the password attribute
	conn = psycopg2.connect("dbname = 'Database1' user='postgres' password='' host = 'localhost' port = '5432'")
	cur = conn.cursor()
	cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity, price, item))
	conn.commit()
	conn.close()

#create_table()
#insert('Coffee glass', 10, 200.3)
#insert('Water Glass', 5, 100)
#insert('Beer Glass', 20, 5000)
#delete('Beer Glass')
#update(10, 1500, 'Water Glass')
#print(view())

