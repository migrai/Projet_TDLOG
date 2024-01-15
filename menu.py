import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget
from PyQt5.QtGui import QIcon
from gamewindow import GameWindow
from menuLogic import MenuLogic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Adds a vertical layout to the main window
        vertical_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        vertical_layout.addWidget(self.label)
        vertical_layout.addWidget(self.label, alignment=QtCore.Qt.AlignHCenter)

        # Adds buttons to central window
        self.morpion_button = QtWidgets.QPushButton(
            "Morpion", self.centralwidget
        )
        self.morpion_button.setIcon(QtGui.QIcon("icon_1.png"))
        vertical_layout.addWidget(self.morpion_button)

        self.meta_button = QtWidgets.QPushButton(
            "Méta-Morpion", self.centralwidget
        )
        self.meta_button.setIcon(QtGui.QIcon("icon_2.png"))
        vertical_layout.addWidget(self.meta_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        vertical_layout.addWidget(self.exit_button)

        # Names each button and defines what each does
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.menuOptions.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))
        self.morpion_button.clicked.connect(
            lambda: MenuLogic.morpion_clicked(self, MainWindow)
            )
        self.meta_button.clicked.connect(
            lambda: MenuLogic.meta_morpion_clicked(self, MainWindow)
            )
        self.exit_button.clicked.connect(MainWindow.close)
    
        self.original_geometry = MainWindow.geometry()
        self.vertical_layout = vertical_layout

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3Morpion"))
        self.label.setText(_translate("MainWindow", "Main Menu"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def save_geometry(self):
        return self.original_geometry

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #table = GameWindow(ui)

    MainWindow.show()
    sys.exit(app.exec_())