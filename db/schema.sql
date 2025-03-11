#SQL-script för att skapa tabeller

CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique user ID
	name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	password TEXT NOT NULL,
	balance REAL DEFAULT 0.0 -- user balance
);
