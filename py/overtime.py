# overtime.py

import sqlite3

connection = sqlite3.connect('overtime.db')
cursor = connection.cursor()

# Buat tabel lembur
cursor.execute('''
    CREATE TABLE IF NOT EXISTS lembur (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        id_karyawan TEXT,
        jabatan TEXT,
        waktu TEXT
    )
''')

connection.commit()
connection.close()
