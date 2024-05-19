# Import sqlite3
import sqlite3

def create_database():
    # Membuat koneksi ke database overtime.db
    connection = sqlite3.connect('adikazahran.db')
    
    # Membuat objek cursor untuk menjalankan perintah SQL
    cursor = connection.cursor()

    # Contoh: Membuat tabel lembur
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lembur (
            id_karyawan INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,            
            jabatan TEXT,
            waktu TEXT
        )
    ''')

    # Commit perubahan ke database
    connection.commit()

    # Menutup koneksi ke database
    connection.close()
