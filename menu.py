import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget
from PyQt5.QtGui import QIcon
from menuLogic import MenuLogic
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.difficultyMod = 0

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
        self.menuDiff = QtWidgets.QMenu(self.menubar)
        self.menuDiff.setObjectName("menuDiff")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Diffrand = QtWidgets.QAction(MainWindow)
        self.Diffrand.setObjectName("Diffrand")
        self.DiffbestMove = QtWidgets.QAction(MainWindow)
        self.DiffbestMove.setObjectName("DiffbestMove")

        self.menuDiff.addAction(self.Diffrand)
        self.menuDiff.addAction(self.DiffbestMove)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuDiff.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Diffrand.triggered.connect(lambda: self.set_diff(0))
        self.DiffbestMove.triggered.connect(lambda: self.set_diff(1))
        self.morpion_button.clicked.connect(
            lambda: MenuLogic.morpion_clicked(self, MainWindow, self.difficultyMod)
            )
        self.meta_button.clicked.connect(
            lambda: MenuLogic.meta_morpion_clicked(self, MainWindow, self.difficultyMod)
            )
        self.exit_button.clicked.connect(MainWindow.close)
    
        self.original_geometry = MainWindow.geometry()
        self.vertical_layout = vertical_layout

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3Morpion"))
        self.label.setText(_translate("MainWindow", "Main Menu"))
        self.menuOptions.setTitle(_translate("MainWindow", "Welcome"))
        self.menuDiff.setTitle(_translate("MainWindow", "Difficulty"))
        self.Diffrand.setText(_translate("MainWindow", "Easy"))
        self.Diffrand.setShortcut(_translate("MainWindow", "Ctrl+1"))
        self.DiffbestMove.setText(_translate("MainWindow", "Hard"))
        self.DiffbestMove.setShortcut(_translate("MainWindow", "Ctrl+2"))
        

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
    
    def set_diff(self, diff):
        self.difficultyMod = diff
        print(self.difficultyMod)
        return self.difficultyMod

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    #table = GameWindow(ui)

    MainWindow.show()
    sys.exit(app.exec_())