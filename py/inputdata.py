# inputdata.py

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        _translate = QtCore.QCoreApplication.translate

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_nama = QtWidgets.QLabel(self.centralwidget)
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setObjectName("label_nama")
        self.label_nama.setText(_translate("MainWindow", "Nama"))
        self.verticalLayout.addWidget(self.label_nama)

        self.nama_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_input.setObjectName("nama_input")
        self.verticalLayout.addWidget(self.nama_input)

        self.label_id_karyawan = QtWidgets.QLabel(self.centralwidget)
        self.label_id_karyawan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id_karyawan.setObjectName("label_id_karyawan")
        self.label_id_karyawan.setText(_translate("MainWindow", "ID Karyawan"))
        self.verticalLayout.addWidget(self.label_id_karyawan)

        self.id_karyawan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.id_karyawan_input.setObjectName("id_karyawan_input")
        self.verticalLayout.addWidget(self.id_karyawan_input)

        self.label_jabatan = QtWidgets.QLabel(self.centralwidget)
        self.label_jabatan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jabatan.setObjectName("label_jabatan")
        self.label_jabatan.setText(_translate("MainWindow", "Jabatan"))
        self.verticalLayout.addWidget(self.label_jabatan)

        self.jabatan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.jabatan_input.setObjectName("jabatan_input")
        self.verticalLayout.addWidget(self.jabatan_input)

        self.label_waktu = QtWidgets.QLabel(self.centralwidget)
        self.label_waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_waktu.setObjectName("label_waktu")
        self.label_waktu.setText(_translate("MainWindow", "Waktu"))
        self.verticalLayout.addWidget(self.label_waktu)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setObjectName("submit_button")
        self.verticalLayout.addWidget(self.submit_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the button click event to the create_data method
        self.submit_button.clicked.connect(self.create_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Input Data"))
        self.label.setText(_translate("MainWindow", "Input Data"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))

    def create_data(self):
        # Dapatkan data dari kolom input
        nama = self.nama_input.text()
        id_karyawan = self.id_karyawan_input.text()
        jabatan = self.jabatan_input.text()
        waktu = self.dateTimeEdit.dateTime().toString()

        # Masukkan data ke dalam database
        connection = sqlite3.connect('overtime.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO lembur (nama, id_karyawan, jabatan, waktu) VALUES (?, ?, ?, ?)",
                       (nama, id_karyawan, jabatan, waktu))
        connection.commit()
        connection.close()

        print("Data berhasil dibuat.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
