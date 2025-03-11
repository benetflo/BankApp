#SQL-script för att skapa tabeller

CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique user ID
	name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	balance REAL DEFAULT 0.0 -- user balance
);

CREATE TABLE IF NOT EXISTS accounts (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique account ID
	user_id INTEGER NOT NULL, -- matche account to a user in users table
	account_type TEXT NOT NULL,
	balance REAL NOT NULL DEFAULT 0.0, -- account balance. start with 0.0 as standard
	FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- if user is removed == account removed
);
