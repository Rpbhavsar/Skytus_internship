import sqlite3
conn=sqlite3.connect("transactions.db")
cursor=conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_name TEXT NOT NULL,
    balance INTEGER NOT NULL CHECK(balance >= 0)
    )  
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS transfer(
    transfer_ref TEXT PRIMARY KEY,
    from_account INTEGER NOT NULL,
    to_account INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    FOREIGN KEY (from_account) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account) REFERENCES accounts(account_id)
    )
 ''')

accounts=[
    (1,"Ronit",10000),
    (2,"Hem",2000),
    (3,"Karan",3000)
]

cursor.executemany("INSERT OR IGNORE INTO accounts (account_id, account_name, balance) VALUES (?, ?, ?)", accounts)

conn.commit()


# 1.Start a transaction and insert a record
print("===Transaction and Rollback===")

conn.execute("Begin")
cursor.execute('''INSERT INTO accounts VALUES(?,?,?)''',(4,"Rohit",4000))

print("Temporary record inserted ")


# 2.Rollback changes
conn.rollback()
cursor.execute('''SELECT * FROM accounts WHERE account_id=4 ''')

print("After rollback:",cursor.fetchone())


# 3.Commit a valid transaction
print("\n ===Commit valid transaction===")

conn.execute("Begin")
cursor.execute('''INSERT OR IGNORE INTO accounts VALUES (?,?,?)''',(5,"Amit",5000)
 )

conn.commit()

print("Valid account commited successfully")


# 4.Demonstrate money transfer using a transaction
def transfer_money(from_id, to_id, amount, transfer_ref):
    try:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        conn.execute("BEGIN")

        # Avoid processing the same transfer twice
        cursor.execute("""
        SELECT transfer_ref
        FROM transfer
        WHERE transfer_ref = ?
        """, (transfer_ref,))

        if cursor.fetchone():
            conn.rollback()
            print("This transfer was already completed.")
            return

        # Check source account
        cursor.execute("""
        SELECT balance FROM accounts
        WHERE account_id = ?
        """, (from_id,))

        sender = cursor.fetchone()

        # Check destination account
        cursor.execute("""
        SELECT balance FROM accounts
        WHERE account_id = ?
        """, (to_id,))

        receiver = cursor.fetchone()

        if sender is None or receiver is None:
            raise ValueError("Account not found.")

        if sender[0] < amount:
            raise ValueError("Insufficient balance.")

        # Debit sender
        cursor.execute("""
        UPDATE accounts
        SET balance = balance - ?
        WHERE account_id = ?
        """, (amount, from_id))

        # Credit receiver
        cursor.execute("""
        UPDATE accounts
        SET balance = balance + ?
        WHERE account_id = ?
        """, (amount, to_id))

        # Record completed transfer in same transaction
        cursor.execute("""
        INSERT INTO transfer
        VALUES (?, ?, ?, ?)
        """, (transfer_ref, from_id, to_id, amount))

        conn.commit()
        print("Transfer completed successfully!")

    except (sqlite3.Error, ValueError) as error:
        conn.rollback()
        print("Transfer failed:", error)


print("\n=== Money Transfer ===")

transfer_money(1, 2, 2000, "DEMO-001")


# 5. Display final account balances
print("\n=== Final Account Balances ===")

cursor.execute("""
SELECT account_id, account_name, balance
FROM accounts
ORDER BY account_id
""")

for account_id, acc_name, balance in cursor.fetchall():
    print(account_id, acc_name, ":", balance)

conn.close()