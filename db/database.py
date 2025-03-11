# Kod för att hantera SQLITE-anslutningen

# .cursor kan utföra uppgifter i databasen

import sqlite3


def connect_db():
	return sqlite3.connect("bankapp.db") # if not exists create database file

def create_tables_from_schema():
	conn = connect_db()
	cursor = conn.cursor()
	try:
		with open('db/schema.sql', 'r') as f:
			sql_script = f.read()

		cursor.executescript(sql_script)
		conn.commit()
		return True

	except FileNotFoundError:
		return False
	finally:
		conn.close()


def add_user(name, email, password):
	conn = connect_db()
	cursor = conn.cursor()
	try:
		cursor.execute('''
		INSERT INTO users (name, email, password)
		VALUES (?, ?, ?)
		''', (name, email, password))
		conn.commit() # commit to database
		return True
	except:
		return False
	finally:
		conn.close() # close connection to database

def delete_user(user_id):

	try:
		conn = connect_db()
		cursor = conn.cursor()
		cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
		conn.commit()
		return True
	except:
		return False
	finally:
		conn.close()



def get_user_by_email(email):
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
	user = cursor.fetchone() # gets first matching user
	conn.close()
	return user




