import pandas as pd
import sqlite3
import os

# Set base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'database', 'ecom.db'))
DATA_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'data'))

# ✅ 1. FUNCTION TO CREATE DATABASE FROM CSVs
def create_database():
    csvs = {
        'ad_sales': os.path.join(DATA_PATH, 'ad_sales_metrics.csv'),
        'total_sales': os.path.join(DATA_PATH, 'total_sales_metrics.csv'),
        'eligibility': os.path.join(DATA_PATH, 'eligibility_table.csv')
    }

    # Check that all files exist
    for name, path in csvs.items():
        if not os.path.exists(path):
            print(f"❌ File not found: {path}")
            return

    # Create database
    try:
        conn = sqlite3.connect(DB_PATH)
        for table, path in csvs.items():
            df = pd.read_csv(path)
            df.to_sql(table, conn, if_exists='replace', index=False)
            print(f"✅ Imported {table} from {path}")
        conn.close()
        print(f"\n🎉 Database created successfully at: {DB_PATH}")
    except Exception as e:
        print(f"❌ Error creating database: {e}")

# ✅ 2. FUNCTION TO QUERY DATABASE
def query_db(sql):
    try:
        if not sql or not isinstance(sql, str):
            return [], ["❌ Invalid SQL query."]
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description]
        conn.close()
        return cols, rows
    except Exception as e:
        return [], [f"❌ Unexpected Error: {e}"]


# ✅ 3. OPTIONALLY RUN THIS SCRIPT STANDALONE
if __name__ == "__main__":
    print("📦 Creating database from CSV files...")
    create_database()
