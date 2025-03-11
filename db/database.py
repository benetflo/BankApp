# Kod för att hantera SQLITE-anslutningen

# .cursor kan utföra uppgifter i databasen

import sqlite3


def connect_db():
	return sqlite3.connect("bankapp.db") # if not exists create database file


def add_user(name, email, password):
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute('''
	INSERT INTO users (name, email, password)
	VALUES (?, ?, ?)
	''', (name, email, password))
	conn.commit() # commit to database
	conn.close() # close connection to database

def delete_user(user_id):
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
	conn.commit()
	conn.close()



def get_user_by_email(email):
	conn = connect_db()
	cursor = conn.cursor()
	cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
	user = cursor.fetchone() # gets first matching user
	conn.close()
	return user




