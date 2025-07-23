import sqlite3

con = sqlite3.connect('database/ecom.db')  # Adjust path if needed
tables = con.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
print("Tables:", tables)
for t in tables:
    print(f"\nColumns for {t[0]}:")
    cols = con.execute(f"PRAGMA table_info({t[0]})").fetchall()
    for col in cols:
        print(col)
con.close()
