
import sqlite3
from datetime import datetime


# Create database and table
def create_table():
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date_time TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Save BMI record
def save_record(name, weight, height, bmi, category):
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category, date_time)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, date_time))

    conn.commit()
    conn.close()


# Get all BMI records
def get_records():
    conn = sqlite3.connect("bmi_records.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM bmi_records ORDER BY id DESC")
    records = cursor.fetchall()

    conn.close()
    return records


# Create table when the file runs
if __name__ == "__main__":
    create_table()
    print("BMI database created successfully!")
