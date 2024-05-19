# Import modul yang diperlukan dari PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Import kelas UI dari modul (inputdata, tampildata, editdata)
from inputdata import Ui_InputData
from tampildata import Ui_TampilData
from editdata import Ui_EditData

# Definisikan kelas Ui_NavigationWindow yang berisi tata letak dan fungsi-fungsi navigasi
class Ui_NavigationWindow(object):
    def setupUi(self, NavigationWindow):
        # Metode untuk mengatur tata letak GUI
        NavigationWindow.setObjectName("NavigationWindow")
        NavigationWindow.resize(800, 600)    

        # Membuat central widget
        self.centralwidget = QtWidgets.QWidget(NavigationWindow)
        self.centralwidget.setObjectName("centralwidget")               

        # Membuat stacked widget untuk menampilkan halaman-halaman yang berbeda
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.stackedWidget.setObjectName("stackedWidget")

        # Tambahkan halaman-halaman dari modul terpisah ke dalam stacked widget
        self.ui_input_data = Ui_InputData()
        input_data_page = QtWidgets.QMainWindow()
        self.ui_input_data.setupUi(input_data_page)
        self.stackedWidget.addWidget(input_data_page)        

        self.ui_tampil_data = Ui_TampilData()
        tampil_data_page = QtWidgets.QMainWindow()
        self.ui_tampil_data.setupUi(tampil_data_page)
        self.stackedWidget.addWidget(tampil_data_page)

        self.ui_edit_data = Ui_EditData()
        edit_data_page = QtWidgets.QMainWindow()
        self.ui_edit_data.setupUi(edit_data_page)
        self.stackedWidget.addWidget(edit_data_page)

        # Mengatur Tombol untuk Navigasi
        self.ui_input_data_button = QtWidgets.QPushButton(QtGui.QIcon('add.png'), "Input Data", self.centralwidget)
        self.ui_input_data_button.clicked.connect(self.show_input_data_page)

        self.ui_tampil_data_button = QtWidgets.QPushButton(QtGui.QIcon('search.png'), "Tampil Data", self.centralwidget)
        self.ui_tampil_data_button.clicked.connect(self.show_tampil_data_page)

        self.ui_edit_data_button = QtWidgets.QPushButton(QtGui.QIcon('update.png'), "Edit Data", self.centralwidget)
        self.ui_edit_data_button.clicked.connect(self.show_edit_data_page)
        
        # Mengatur bagian layout pada kelas Ui_NavigationWindow
        layout = QtWidgets.QGridLayout(self.centralwidget)
        layout.addWidget(self.ui_input_data_button, 0, 0)
        layout.addWidget(self.ui_tampil_data_button, 0, 1)
        layout.addWidget(self.ui_edit_data_button, 0, 2)
        layout.addWidget(self.stackedWidget, 1, 0, 1, 3)  

        # Mengatur central widget untuk QMainWindow
        NavigationWindow.setCentralWidget(self.centralwidget)

        # Membuat menu bar dan status bar
        self.menubar = QtWidgets.QMenuBar(NavigationWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        NavigationWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(NavigationWindow)
        self.statusbar.setObjectName("statusbar")
        NavigationWindow.setStatusBar(self.statusbar)

        # Memanggil metode retranslateUi untuk mengatur teks terjemahan
        self.retranslateUi(NavigationWindow)
        QtCore.QMetaObject.connectSlotsByName(NavigationWindow)
    
    # Metode untuk mengatur teks terjemahan
    def retranslateUi(self, NavigationWindow):
        _translate = QtCore.QCoreApplication.translate
        NavigationWindow.setWindowTitle(_translate("NavigationWindow", "Program Lembur Karyawan"))

    # Metode untuk menampilkan halaman input data
    def show_input_data_page(self):
        self.stackedWidget.setCurrentIndex(0)

    # Metode untuk menampilkan halaman tampil data
    def show_tampil_data_page(self):
        self.stackedWidget.setCurrentIndex(1)

    # Metode untuk menampilkan halaman edit data
    def show_edit_data_page(self):
        self.stackedWidget.setCurrentIndex(2)


if __name__ == "__main__":
    import sys
    # Inisialisasi aplikasi Qt
    app = QtWidgets.QApplication(sys.argv)
    # Inisialisasi objek QMainWindow
    NavigationWindow = QtWidgets.QMainWindow()
    # Inisialisasi objek Ui_NavigationWindow
    ui = Ui_NavigationWindow()
    # Memanggil metode setupUi untuk mengatur tata letak GUI
    ui.setupUi(NavigationWindow)
    # Tampilkan GUI 
    NavigationWindow.show()
    # Running aplikasi
    sys.exit(app.exec_())
