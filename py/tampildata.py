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

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nama"])
        self.verticalLayout.addWidget(self.tableWidget)

        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setObjectName("refresh_button")
        self.verticalLayout.addWidget(self.refresh_button)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the button click event to the show_data method
        self.refresh_button.clicked.connect(self.show_data)

        # Tampilkan data saat antarmuka pengguna dimuat
        self.show_data()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tampil Data"))
        self.label.setText(_translate("MainWindow", "Data Lembur"))
        self.refresh_button.setText(_translate("MainWindow", "Refresh"))

    def show_data(self):
        # Dapatkan data dari database
        connection = sqlite3.connect('overtime.db')
        cursor = connection.cursor()
        cursor.execute("SELECT id, nama, id_karyawan, jabatan, waktu FROM lembur")
        data = cursor.fetchall()
        connection.close()

        # Isi tabel dengan data
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))  # Sesuaikan dengan jumlah kolom di database

        column_headers = ["ID", "Nama", "ID Karyawan", "Jabatan", "Waktu"]
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        for row_num, row_data in enumerate(data):
            for col_num, col_data in enumerate(row_data):
                self.tableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(col_data)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())