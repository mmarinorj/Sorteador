# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
import random
import copy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 361)
        MainWindow.setMinimumSize(QtCore.QSize(565, 361))
        MainWindow.setMaximumSize(QtCore.QSize(565, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sorteio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(44, 79, 38);\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
        "   background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                      stop:0 #20301d, stop: 0.5 #386231,\n"
        "                                      stop: 0.6 #20301d, stop:1 #20301d);\n"
        "   color: rgb(255,255,255);\n"
        "    border: 1px solid  rgb(73, 127, 63);\n"
        "    border-bottom-color: rgb(73, 127, 63); /* same as the pane color */\n"
        "    border-top-left-radius: 2px;\n"
        "    border-top-right-radius: 2px;\n"
        "    min-width:14ex;\n"
        "    padding: 6px;\n"
        "}\n"
        "QTabBar::tab:selected {\n"
        "   background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
        "                                      stop:0 #497f3f, stop: 0.5 rgb(65, 113, 56),\n"
        "                                      stop: 0.6 #497f3f, stop:1 #497f3f);\n"
        "  /* background: rgb(73, 127, 63);*/\n"
        "   color: rgb(255,255,255);\n"
        "   \n"
        "}\n"
        "\n"
        "QTabWidget::pane {\n"
        "    border: 2px solid rgb(73, 127, 63);\n"
        "}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(21, 170, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: cyan;")
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(126, 240, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(21)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton.setShortcut("")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setEnabled(True)
        self.lcdNumber.setGeometry(QtCore.QRect(136, 20, 291, 131))
        self.lcdNumber.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setDigitCount(4)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setProperty("intValue", 8888)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(30, 235, 51, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sorteio.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 101, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 120, 101, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(470, 235, 51, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("sorteio.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(440, 50, 21, 25))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("1st - ouro.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(440, 80, 21, 25))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("2st - prata.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(440, 110, 21, 25))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("3st - bronze.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(440, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(445, 140, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(470, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(470, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(470, 110, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"    color: white;\n"
"    background-color: rgb(46, 69, 42);    \n"
"    font: 75 bold 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #294723, stop: 0.5 #386231,\n"
"                                      stop: 0.6 #294723, stop:1 #294723);\n"
"    color: white;\n"
"    padding-left:0px;\n"
"    border: 0.5px solid #294723;\n"
"}\n"
"QTableView QTableCornerButton::section {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 #294723, stop: 0.5 #386231,\n"
"                                      stop: 0.6 #294723, stop:1 #294723);\n"
"    border: 0.5px solid #294723;\n"
"}")
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout_4.addWidget(self.spinBox)
        self.verticalLayout_3.addWidget(self.frame_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sorteador 1.0 - @mmarinorj"))
        self.pushButton.setText(_translate("MainWindow", "SORTEAR"))
        self.radioButton.setText(_translate("MainWindow", "SORTEIO LIVRE"))
        self.radioButton_2.setText(_translate("MainWindow", "TOP 5"))
        self.radioButton_3.setText(_translate("MainWindow", "TOP 10"))
        self.radioButton_4.setText(_translate("MainWindow", "OS MELHORES"))
        self.label_3.setText(_translate("MainWindow", "MODO DE SORTEIO:"))
        self.label_8.setText(_translate("MainWindow", "TOP 3:"))
        self.pushButton_4.setText(_translate("MainWindow", "RESULTADOS"))
        self.label_9.setText(_translate("MainWindow", "-"))
        self.label_10.setText(_translate("MainWindow", "-"))
        self.label_11.setText(_translate("MainWindow", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Sorteio"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Número"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nome"))
        self.pushButton_2.setText(_translate("MainWindow", "ADICIONAR"))
        self.pushButton_3.setText(_translate("MainWindow", "CARREGAR"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Ajustes"))
################################ INICIO BLOCO PRÓPRIO ##################################################################
        self.statusBar.showMessage("   *****Contatos: @mmarinorj | mmarinorj@gmail.com (e-mail / PIX) | www.github."
                                   "com/mmarinorj*****")
        self.statusBar.setStyleSheet("color: black")
        self.lcdNumber.display("0000")
        self.flag1 = False
        self.contador1 = 0
        self.contador2 = -1
        self.tempo = 0
        
        self.pushButton.clicked.connect(self.Sortear)
        self.pushButton_2.clicked.connect(self.Adicionar)
        self.pushButton_3.clicked.connect(self.Carregar)
        self.spinBox.setValue(3)
        
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.ShowTime)
        self.timer.start(50)
        self.base = []
        self.temp = copy.deepcopy(self.base)
        if self.base == []:
            self.pushButton.setEnabled(False)
            self.pushButton.setStyleSheet("color: gray")
    
    def ShowTime(self):
        if self.flag1:
            self.contador1 += 1111
            self.lcdNumber.display(self.contador1)
            if self.contador1 > 9999:
                self.contador1 = 3157
        if int(time.time()) - self.tempo == 5:
            self.flag1 = False
            self.lcdNumber.display(self.sorteado[0])
            self.label.setText(self.sorteado[1])
            self.lcdNumber.setStyleSheet("color: yellow; background-color: black; border: 3px solid white;")
            if self.contador2 == 0:
                temp = (self.sorteado[1].split(" "))[0].upper()
                self.label_9.setText(temp)
            if self.contador2 == 1:
                temp = (self.sorteado[1].split(" "))[0].upper()
                self.label_10.setText(temp)
            if self.contador2 == 2:
                temp = (self.sorteado[1].split(" "))[0].upper()
                self.label_11.setText(temp)
            if len(self.temp) > 0:
                self.pushButton.setStyleSheet("color: white")
                self.pushButton.setEnabled(True)
                self.tabWidget.setEnabled(True)
            else:
                self.lcdNumber.setEnabled(False)
                self.label.setEnabled(False)
                self.tabWidget.setEnabled(True)
    
    def Sortear(self):
        self.lcdNumber.setStyleSheet("color: white; background-color: black; border: 3px solid white;")
        self.sorteado = random.choice(self.temp)
        self.temp.remove(self.sorteado)
        self.tableWidget.clear()
        self.tableWidget.setHorizontalHeaderLabels(["Número", "Nome"])
        self.tableWidget.setRowCount(len(self.temp))
        for i, n in enumerate(self.temp):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(n[0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(n[1]))
        if not self.flag1:
            self.flag1 = True
        self.tempo = int(time.time())
        self.pushButton.setEnabled(False)
        self.tabWidget.setEnabled(False)
        self.pushButton.setStyleSheet("color: gray")
        self.label.clear()
        if self.contador2 > 2:
            pass
        else:
            self.contador2 += 1
        if self.contador2 == self.tableWidget.rowCount():
            self.contador2 = -1
            
    def Adicionar(self):
        self.tableWidget.setRowCount(int(self.spinBox.text()))
        if int(self.spinBox.text()) < 2:
            pass
        else:
            for i in range(int(self.spinBox.text())):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(i + 1)))
            temp = self.tableWidget.rowCount()
            self.base.clear()
            self.temp.clear()
            for i in range(temp):
                if self.tableWidget.item(i, 0) == None:
                    data1 = "0"
                else:
                    data1 = self.tableWidget.item(i, 0).text()
                if self.tableWidget.item(i, 1) == None:
                    data2 = ""
                else:
                    data2 = self.tableWidget.item(i, 1).text()
                lista_temp = [int(data1), data2]
                self.base.append(lista_temp)
                if self.base[0][0] == 0:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setStyleSheet("color: gray")
                else:
                    self.pushButton.setStyleSheet("color: white")
                    self.pushButton.setEnabled(True)
                    self.temp = copy.deepcopy(self.base)
        self.label_9.setText("-")
        self.label_10.setText("-")
        self.label_11.setText("-")
        self.label.clear()
        self.lcdNumber.display('0000')
    
    def Carregar(self):
        listasorteio = []
        arquivo = QtWidgets.QFileDialog.getOpenFileName(None, "Carregar Arquivo de Texto", "",
                                                        "TXT files (*.txt)")[0]
        with open(arquivo, encoding='utf-8', mode='r') as linha:
            lista1 = linha.read().splitlines()
        for i in lista1:
            a, b = i.split('=')
            temporario = []
            temporario.append(a)
            temporario.append(b)
            listasorteio.append(temporario)
        self.temp = copy.deepcopy(listasorteio)
        self.base = copy.deepcopy(listasorteio)
        self.tableWidget.setRowCount(len(listasorteio))
        for i, n in enumerate(listasorteio):
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(n[0]))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(n[1]))
        temp = self.tableWidget.rowCount()
        self.base.clear()
        self.temp.clear()
        for i in range(temp):
            if self.tableWidget.item(i, 0) == None:
                data1 = "0"
            else:
                data1 = self.tableWidget.item(i, 0).text()
            if self.tableWidget.item(i, 1) == None:
                data2 = ""
            else:
                data2 = self.tableWidget.item(i, 1).text()
            lista_temp = [int(data1), data2]
            self.base.append(lista_temp)
            if self.tableWidget.rowCount() < 2:
                pass
            else:
                if self.base[0][0] == 0:
                    self.pushButton.setEnabled(False)
                    self.pushButton.setStyleSheet("color: gray")
                else:
                    self.pushButton.setStyleSheet("color: white")
                    self.pushButton.setEnabled(True)
                    self.temp = copy.deepcopy(self.base)
        self.label_9.setText("-")
        self.label_10.setText("-")
        self.label_11.setText("-")
        self.label.clear()
        self.lcdNumber.display('0000')
################################ FINAL BLOCO PRÓPRIO ###################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
