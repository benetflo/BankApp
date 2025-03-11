


-- Skapa users-tabellen
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unikt användar-ID
    name TEXT NOT NULL,                     -- Namn på användaren
    email TEXT NOT NULL UNIQUE,             -- Unik e-postadress
    password TEXT NOT NULL,                 -- Lösenord för användaren
    balance REAL DEFAULT 0.0                -- Saldo för användaren
);

-- Skapa accounts-tabellen
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unikt kontonummer
    user_id INTEGER NOT NULL,              -- Referens till användare
    account_type TEXT NOT NULL,            -- Typ av konto (t.ex. Sparkonto, Lönekonto)
    balance REAL NOT NULL DEFAULT 0.0,     -- Konto saldo
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE -- Om användaren tas bort, tas kontot också bort
);

