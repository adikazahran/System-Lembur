# Import semua modul yang diperlukan dari PyQt5 dan sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# Definisikan kelas Ui_EditData yang berisi tata letak dan sebuah GUI
class Ui_EditData(object):
    def setupUi(self, EditData):
        # Metode untuk mengatur tata letak GUI
        EditData.setObjectName("EditData")
        EditData.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(EditData)
        self.centralwidget.setObjectName("centralwidget")

        # Menambahkan background image
        self.centralwidget.setStyleSheet("background-image: url('img.jpeg'); background-position: center;")

        # Penggunaan layout vertikal untuk menata elemen-elemen GUI secara vertikal        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Membuat label dan input field untuk "Nama"
        self.label_nama = QtWidgets.QLabel(self.centralwidget)
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setObjectName("label_nama")
        self.label_nama.setText("Nama:")
        self.label_nama.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_nama)
        self.nama_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_input.setObjectName("nama_input")    
        self.verticalLayout.addWidget(self.nama_input)

        # Membuat label dan combo box untuk "Pilih ID Karyawan"
        self.label_pilih_id = QtWidgets.QLabel(self.centralwidget)
        self.label_pilih_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pilih_id.setObjectName("label_pilih_id")
        self.label_pilih_id.setText("Pilih ID Karyawan:")
        self.label_pilih_id.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_pilih_id)
        self.comboBox_id_karyawan = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_id_karyawan.setObjectName("comboBox_id_karyawan")
        self.verticalLayout.addWidget(self.comboBox_id_karyawan)

        # Membuat label dan input field untuk "Jabatan"
        self.label_jabatan = QtWidgets.QLabel(self.centralwidget)
        self.label_jabatan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jabatan.setObjectName("label_jabatan")
        self.label_jabatan.setText("Jabatan:")
        self.label_jabatan.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_jabatan)
        self.jabatan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.jabatan_input.setObjectName("jabatan_input")    
        self.verticalLayout.addWidget(self.jabatan_input)

        # Membuat label dan input field untuk "Waktu"
        self.label_waktu = QtWidgets.QLabel(self.centralwidget)
        self.label_waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_waktu.setObjectName("label_waktu")
        self.label_waktu.setText("Waktu:")
        self.label_waktu.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_waktu)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.dateTimeEdit)

        # Tambahkan tombol "Refresh" ke dalam layout vertikal
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.refresh_button)        

        # Membuat tombol "Update" ke layout vertikal
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.update_button.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.update_button)

        # Inisialisasi nilai variabel id_to_update sebagai None
        self.id_to_update = None

        # Mengatur widget utama sebagai central widget
        EditData.setCentralWidget(self.centralwidget)

        # Memanggil metode retranslateUi untuk mengatur teks terjemahan
        self.retranslateUi(EditData)
        QtCore.QMetaObject.connectSlotsByName(EditData)

        # Mengisi combo box dengan ID karyawan dari database saat Interface pengguna diproses
        self.fill_id_karyawan_combobox()

        # Connect the button click event to the fill_id_karyawan_combobox method
        self.refresh_button.clicked.connect(self.fill_id_karyawan_combobox)        

        # Menghubungkan tombol "Update" dengan metode update_data
        self.update_button.clicked.connect(self.update_data)

    # Metode untuk mengatur teks terjemahan
    def retranslateUi(self, EditData):
        _translate = QtCore.QCoreApplication.translate
        EditData.setWindowTitle(_translate("EditData", "Edit Data Lembur Karyawan"))
        self.label_nama.setText(_translate("EditData", "Nama"))
        self.label_jabatan.setText(_translate("EditData", "Jabatan"))
        self.label_waktu.setText(_translate("EditData", "Waktu"))
        self.refresh_button.setText(_translate("EditData", "Refresh"))
        self.update_button.setText(_translate("EditData", "Update"))                

    # Metode untuk mengisi combo box dengan ID karyawan dari database
    def fill_id_karyawan_combobox(self):
        # Mengisi combo box dengan ID karyawan dari database
        connection = sqlite3.connect('adikazahran.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT id_karyawan FROM lembur")
        id_karyawan_list = [str(row[0]) for row in cursor.fetchall()]
        connection.close()

        # Membersihkan combo box sebelum menambahkan item baru
        self.comboBox_id_karyawan.clear()
        self.comboBox_id_karyawan.addItems(id_karyawan_list)

    # Metode yang akan dipanggil saat tombol "Update" ditekan
    def update_data(self):
        # Untuk mendapatkan data dari kolom input
        nama = self.nama_input.text()
        id_karyawan_to_update = self.comboBox_id_karyawan.currentText()  # Ambil ID Karyawan yang dipilih
        jabatan = self.jabatan_input.text()
        waktu = self.dateTimeEdit.dateTime().toString()

        # Memperbarui data dalam database
        connection = sqlite3.connect('adikazahran.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE lembur SET nama = ?, jabatan = ?, waktu = ? WHERE id_karyawan = ?",
                   (nama, jabatan, waktu, id_karyawan_to_update))
        connection.commit()
        connection.close()

        # Tampilkan pesan MessageBox
        self.show_update_message()

        # Print pesan ke konsol
        print("Data berhasil diperbarui.")

        # Membersihkan input fields
        self.clear_input_fields()

    # Metode untuk menampilkan pesan keberhasilan update
    def show_update_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Data Sudah Ter-Update")
        msg_box.setWindowTitle("Sukses")
        msg_box.exec_()
    
    # Metode untuk membersihkan input fields
    def clear_input_fields(self):
        self.nama_input.clear()
        self.jabatan_input.clear()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime()) 


if __name__ == "__main__":
    import sys
    # Inisialisasi aplikasi Qt
    app = QtWidgets.QApplication(sys.argv)
    # Inisialisasi objek QMainWindow
    EditData = QtWidgets.QMainWindow()
    # Inisialisasi objek Ui_EditData
    ui = Ui_EditData()
    # Panggil metode setupUi untuk mengatur tata letak GUI
    ui.setupUi(EditData)
    # Tampilkan GUI
    EditData.show()
    # Running aplikasi
    sys.exit(app.exec_())
