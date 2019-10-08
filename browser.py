import os
import sys
from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from PyQt5.QtCore import QUrl

# from PYMONGO import logindb



class MainWindow:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.w = QtWidgets.QMainWindow()

        # calling functions
        self.initializeGUI()

        # window properties begin #
        self.w.setWindowTitle("FIRST WINDOW")
        self.w.setGeometry(0, 0, 300, 810)
        self.w.setMaximumHeight(700)
        self.w.setMaximumWidth(1350)
        self.w.setMinimumHeight(500)
        self.w.setMinimumWidth(1350)

        # self.w.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.w.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        # self.w.setWindowFlags(QtCore.Qt.WindowMaximizeButtonHint)

        self.w.setStyleSheet('border:2px solid #4e4e4e; border-radius:10px; background-color: black')
        # window properties end #
        self.w.show()
        sys.exit(self.app.exec_())

        # create a function to initialize the gui and have all graphical interface

    def initializeGUI(self):

        self.Exit_btn = QtWidgets.QPushButton("EXIT", self.w)
        self.Exit_btn.setGeometry(5, 5, 50, 45)
        self.Exit_btn.setStyleSheet('background-color:#f6f6f6')


        self.tabs = QtWidgets.QTabWidget(self.w)
        self.tab1 = QtWidgets.QWidget(self.w)
        self.tab2 = QtWidgets.QWidget(self.w)
        self.tab3 = QtWidgets.QWidget(self.w)

        self.tabs.addTab(self.tab1, "GOOGLE")
        self.tabs.addTab(self.tab2, "SIMULI")
        self.tabs.addTab(self.tab3, "GITHUB")

        self.tabs.setGeometry(6, 50, 1336, 640)
        self.tabs.setStyleSheet(
            'border:2px solid #4e4e4e; border-radius:10px; background-color: green; font-size:12px;')

        self.tab1_layout = QtWidgets.QVBoxLayout(self.w)
        self.tab1.setLayout(self.tab1_layout)
        self.tab2_layout = QtWidgets.QVBoxLayout(self.w)
        self.tab2.setLayout(self.tab2_layout)
        self.tab3_layout = QtWidgets.QVBoxLayout(self.w)
        self.tab3.setLayout(self.tab3_layout)

        self.webView_view = QtWebEngineWidgets.QWebEngineView(self.w)
        self.webView_view.setGeometry(6, 50, 1336, 640)
        self.webView_view.setUrl(QUrl("https://www.google.com"))
        self.tab1_layout.addWidget(self.webView_view)
        self.Exit_btn.clicked.connect(self.QEuit)

        self.webView_view2 = QtWebEngineWidgets.QWebEngineView(self.w)
        self.webView_view2.setGeometry(6, 50, 1336, 640)
        self.webView_view2.setUrl(QUrl("https://www.simuldocs.com/documents/welcome"))
        self.tab2_layout.addWidget(self.webView_view2)
        self.Exit_btn.clicked.connect(self.QEuit)

        self.webView_view3 = QtWebEngineWidgets.QWebEngineView(self.w)
        self.webView_view3.setGeometry(6, 50, 1336, 640)
        self.webView_view3.setUrl(QUrl("https://github.com/"))
        self.tab3_layout.addWidget(self.webView_view3)
        self.Exit_btn.clicked.connect(self.QEuit)





    def QEuit(self):

        self.buttonReply = QtWidgets.QMessageBox.question(self.w, 'Exit', "Quit",
                                                          QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                          QtWidgets.QMessageBox.No)
        if self.buttonReply == QtWidgets.QMessageBox.Yes:
            self.w.close()
        else:
            pass

    def Profile_Picture(self):
        self.U_Label.setText("information>> Profile Picture is clicked")
# lets instantiate a class to the main window
main = MainWindow()
