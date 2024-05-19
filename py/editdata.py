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

        # Create labels for input fields
        self.label_nama = QtWidgets.QLabel(self.centralwidget)
        self.label_nama.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nama.setObjectName("label_nama")
        self.label_nama.setText("Nama:")
        self.verticalLayout.addWidget(self.label_nama)

        self.nama_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_input.setObjectName("nama_input")
        self.verticalLayout.addWidget(self.nama_input)

        

        self.label_pilih_id = QtWidgets.QLabel(self.centralwidget)
        self.label_pilih_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pilih_id.setObjectName("label_pilih_id")
        self.label_pilih_id.setText("Pilih ID Karyawan:")
        self.verticalLayout.addWidget(self.label_pilih_id)

        self.comboBox_id_karyawan = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_id_karyawan.setObjectName("comboBox_id_karyawan")
        self.verticalLayout.addWidget(self.comboBox_id_karyawan)

        

       

        self.label_jabatan = QtWidgets.QLabel(self.centralwidget)
        self.label_jabatan.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jabatan.setObjectName("label_jabatan")
        self.label_jabatan.setText("Jabatan:")
        self.verticalLayout.addWidget(self.label_jabatan)

        self.jabatan_input = QtWidgets.QLineEdit(self.centralwidget)
        self.jabatan_input.setObjectName("jabatan_input")
        self.verticalLayout.addWidget(self.jabatan_input)

        self.label_waktu = QtWidgets.QLabel(self.centralwidget)
        self.label_waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_waktu.setObjectName("label_waktu")
        self.label_waktu.setText("Waktu:")
        self.verticalLayout.addWidget(self.label_waktu)

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)

        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setObjectName("update_button")
        self.verticalLayout.addWidget(self.update_button)

        self.id_to_update = None

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Isi combo box dengan ID karyawan dari database saat antarmuka pengguna dimuat
        self.fill_id_karyawan_combobox()

        # Connect the button click event to the update_data method
        self.update_button.clicked.connect(self.update_data)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edit Data"))
        self.label_nama.setText(_translate("MainWindow", "Nama"))
        self.label_jabatan.setText(_translate("MainWindow", "Jabatan"))
        self.label_waktu.setText(_translate("MainWindow", "Waktu"))

        self.update_button.setText(_translate("MainWindow", "Update"))

    def fill_id_karyawan_combobox(self):
        # Mengisi combo box dengan ID karyawan dari database
        connection = sqlite3.connect('overtime.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT id_karyawan FROM lembur")
        id_karyawan_list = [str(row[0]) for row in cursor.fetchall()]
        connection.close()

        self.comboBox_id_karyawan.addItems(id_karyawan_list)

    def update_data(self):
        # Dapatkan data dari kolom input
        nama = self.nama_input.text()
        id_karyawan_to_update = self.comboBox_id_karyawan.currentText()  # Ambil ID Karyawan yang dipilih
        jabatan = self.jabatan_input.text()
        waktu = self.dateTimeEdit.dateTime().toString()

        # Perbarui data dalam database
        connection = sqlite3.connect('overtime.db')
        cursor = connection.cursor()
        cursor.execute("UPDATE lembur SET nama = ?, jabatan = ?, waktu = ? WHERE id_karyawan = ?",
                       (nama, jabatan, waktu, id_karyawan_to_update))
        connection.commit()
        connection.close()

        print("Data berhasil diperbarui.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())