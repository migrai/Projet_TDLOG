import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QDesktopWidget
from PyQt5.QtGui import QIcon
from gamewindow import GameWindow
from gamelogic import GameLogic
from PyQt5 import QtCore, QtGui, QtWidgets
from game import Game


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
        self.singleplayer_button = QtWidgets.QPushButton(
            "Singleplayer", self.centralwidget
        )
        self.singleplayer_button.setIcon(QtGui.QIcon("icon_singleplayer.png"))
        vertical_layout.addWidget(self.singleplayer_button)

        self.two_players_button = QtWidgets.QPushButton(
            "Two Players", self.centralwidget
        )
        self.two_players_button.setIcon(QtGui.QIcon("icon_two_players.png"))
        vertical_layout.addWidget(self.two_players_button)

        self.exit_button = QtWidgets.QPushButton("Exit", self.centralwidget)
        self.exit_button.setIcon(QtGui.QIcon("icon_exit.png"))
        vertical_layout.addWidget(self.exit_button)

        # Names each button and defines what each does
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
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
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))
        self.singleplayer_button.clicked.connect(
            lambda: self.clicked("Singleplayer was clicked")
        )
        self.two_players_button.clicked.connect(lambda: GameLogic.play_two_players(self, MainWindow))
        self.exit_button.clicked.connect(MainWindow.close)
    
        self.original_geometry = MainWindow.geometry()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MetaMorpion"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

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
    
    table = GameWindow(ui)

    MainWindow.show()
    sys.exit(app.exec_())