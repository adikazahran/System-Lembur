# Import semua modul yang diperlukan dari PyQt5 dan sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

# Definisikan kelas Ui_TampilData yang berisi tata letak dan sebuah GUI
class Ui_TampilData(object):
    def setupUi(self, TampilData):
        # Metode untuk mengatur tata letak GUI
        TampilData.setObjectName("TampilData")
        TampilData.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(TampilData)
        self.centralwidget.setObjectName("centralwidget")

        # Penggunaan layout vertikal untuk menata elemen-elemen GUI secara vertikal
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Menambahkan background image
        self.centralwidget.setStyleSheet("background-image: url('img.jpeg'); background-position: center;")

        # Membuat label ke layout 
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.label)

        # Membuat tabel untuk menampilkan data
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Nama"])
        self.tableWidget.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.tableWidget)

        # Membuat tombol "Refresh" ke layout 
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setStyleSheet("color: white;")
        self.verticalLayout.addWidget(self.refresh_button)

        # Untuk mengatur widget utama sebagai central widget
        TampilData.setCentralWidget(self.centralwidget)

        # Memanggil metode retranslateUi untuk mengatur teks terjemahan
        self.retranslateUi(TampilData)
        QtCore.QMetaObject.connectSlotsByName(TampilData)

        # Menghubungkan tombol "Refresh" dengan metode show_data
        self.refresh_button.clicked.connect(self.show_data)

        # Memanggil data saat interface pengguna di proses
        self.show_data()

        # Mengatur tabel responsif
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)        

    # Metode untuk mengatur teks 
    def retranslateUi(self, TampilData):
        _translate = QtCore.QCoreApplication.translate
        TampilData.setWindowTitle(_translate("TampilData", "Tampil Data Lembur Karyawan"))
        self.label.setText(_translate("TampilData", "Data Lembur"))
        self.refresh_button.setText(_translate("TampilData", "Refresh"))

    # Metode yang akan dipanggil saat tombol "Refresh" ditekan
    def show_data(self):
        # Untuk mengambil data dari database
        connection = sqlite3.connect('adikazahran.db')
        cursor = connection.cursor()
        cursor.execute("SELECT nama, id_karyawan, jabatan, waktu FROM lembur")
        data = cursor.fetchall()
        connection.close()

        # Untuk Mengecek apakah data tidak kosong
        if not data or not data[0]:
            # Jika data kosong atau tidak ada kolom pertama, atur jumlah kolom menjadi 0
            self.tableWidget.setColumnCount(0)
            return

        # Isi tabel dengan data
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))  # Sesuaikan dengan jumlah kolom di database

        # Untuk menentukan nama kolom untuk header tabel
        column_headers = ["Nama", "ID Karyawan", "Jabatan", "Waktu"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Isi sel tabel dengan data
        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))


if __name__ == "__main__":
    import sys
    # Inisialisasi aplikasi Qt
    app = QtWidgets.QApplication(sys.argv)
    # Inisialisasi objek QMainWindow
    TampilData = QtWidgets.QMainWindow()
    # Inisialisasi objek Ui_TampilData
    ui = Ui_TampilData()
    # Memanggil metode setupUi untuk mengatur tata letak GUI
    ui.setupUi(TampilData)
    # Tampilkan GUI
    TampilData.show()
    # Running aplikasi
    sys.exit(app.exec_())
