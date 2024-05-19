# Import semua modul yang diperlukan dari PyQt5 dan sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# Definisikan kelas Ui_InputData yang berisi tata letak dan sebuah GUI
class Ui_InputData(object):
    def setupUi(self, InputData):
        # Metode untuk mengatur tata letak GUI
        InputData.setObjectName("InputData")
        InputData.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(InputData)
        self.centralwidget.setObjectName("centralwidget")

        # Menambahkan background image 
        self.centralwidget.setStyleSheet("background-image: url('img.jpeg'); background-position: center;")

        # Penggunaan layout vertikal untuk menata elemen-elemen GUI secara vertikal        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        _translate = QtCore.QCoreApplication.translate

        # Membuat label ke layout vertikal
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label)

        # Membuat label dan input field untuk "Nama"
        self.label_nama = QtWidgets.QLabel(self.centralwidget)
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setObjectName("label_nama")
        self.label_nama.setText(_translate("MainWindow", "Nama"))
        self.label_nama.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_nama)
        self.nama_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_input.setObjectName("nama_input")
        self.verticalLayout.addWidget(self.nama_input)

        # Membuat label dan input field untuk "ID Karyawan"
        self.label_id_karyawan = QtWidgets.QLabel(self.centralwidget)
        self.label_id_karyawan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_karyawan.setObjectName("label_id_karyawan")
        self.label_id_karyawan.setText(_translate("MainWindow", "ID Karyawan"))
        self.label_id_karyawan.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_id_karyawan)
        self.id_karyawan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_karyawan_input.setObjectName("id_karyawan_input")
        self.verticalLayout.addWidget(self.id_karyawan_input)

        # Membuat label dan input field untuk "Jabatan"
        self.label_jabatan = QtWidgets.QLabel(self.centralwidget)
        self.label_jabatan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jabatan.setObjectName("label_jabatan")
        self.label_jabatan.setText(_translate("MainWindow", "Jabatan"))
        self.label_jabatan.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_jabatan)
        self.jabatan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.jabatan_input.setObjectName("jabatan_input")
        self.verticalLayout.addWidget(self.jabatan_input)

        # Membuat label dan input field untuk "Waktu"
        self.label_waktu = QtWidgets.QLabel(self.centralwidget)
        self.label_waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_waktu.setObjectName("label_waktu")
        self.label_waktu.setText(_translate("MainWindow", "Waktu"))
        self.label_waktu.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label_waktu)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.dateTimeEdit)

        # Membuat tombol "Submit" ke layout vertikal
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.submit_button)

        # Atur widget utama sebagai central widget
        InputData.setCentralWidget(self.centralwidget)

        # Panggil metode retranslateUi untuk mengatur teks terjemahan
        self.retranslateUi(InputData)
        QtCore.QMetaObject.connectSlotsByName(InputData)

        # Menghubungkan tombol "Submit" dengan metode create_data
        self.submit_button.clicked.connect(self.create_data)

    # Metode untuk mengatur teks terjemahan
    def retranslateUi(self, InputData):
        _translate = QtCore.QCoreApplication.translate
        InputData.setWindowTitle(_translate("InputData", "Input Data Lembur"))
        self.label.setText(_translate("InputData", "Input Data Lembur Karyawan"))
        self.submit_button.setText(_translate("InputData", "Submit"))
     
    # Metode yang akan dipanggil saat tombol "Submit" ditekan
    def create_data(self):
        # Dapatkan data dari kolom input
        nama = self.nama_input.text()
        id_karyawan = self.id_karyawan_input.text()
        jabatan = self.jabatan_input.text()
        waktu = self.dateTimeEdit.dateTime().toString()

        # Masukkan data ke dalam database SQLite
        connection = sqlite3.connect('adikazahran.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO lembur (nama, id_karyawan, jabatan, waktu) VALUES (?, ?, ?, ?)",
                   (nama, id_karyawan, jabatan, waktu))
        connection.commit()
        connection.close()

        # Tampilkan pesan MessageBox
        self.show_success_message()

        # Membersihkan input fields
        self.clear_input_fields()

    # Metode untuk membersihkan input fields
    def clear_input_fields(self):
        self.nama_input.clear()
        self.id_karyawan_input.clear()
        self.jabatan_input.clear()
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())  # Mengatur waktu menjadi waktu saat ini

    # Metode untuk menampilkan pesan keberhasilan
    def show_success_message(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText("Data Sudah Tersimpan")
        msg_box.setWindowTitle("Sukses")
        msg_box.exec_()

    # Print pesan ke konsol
    print("Data berhasil dibuat.")

if __name__ == "__main__":
    import sys
    # Inisialisasi aplikasi Qt
    app = QtWidgets.QApplication(sys.argv)
    # Inisialisasi objek QMainWindow
    InputData = QtWidgets.QMainWindow()
    # Inisialisasi objek Ui_InputData
    ui = Ui_InputData()
    # Memanggil metode setupUi untuk mengatur tata letak GUI
    ui.setupUi(InputData)
    # Tampilkan GUI
    InputData.show()
    # Running aplikasi
    sys.exit(app.exec_())
