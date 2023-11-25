# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main import *
from top5 import *
from top10 import *


class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JanelaTop10()
        self.ui.setupUi(self)
        

class Janela1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JanelaTop5()
        self.ui.setupUi(self)
        
        
class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.jan1 = Janela1()
        self.jan2 = Janela2()
        self.sorteio = self.ui.sorteio
        
        self.ui.pushButton_4.clicked.connect(self.mostraJanela)
    
    def mostraJanela(self):
        if self.ui.radioButton_2.isChecked():
            self.jan1.ui.label_9.setText(self.sorteio[0][1])
            self.jan1.ui.label_10.setText(self.sorteio[1][1])
            self.jan1.ui.label_11.setText(self.sorteio[2][1])
            self.jan1.ui.label_12.setText(self.sorteio[3][1])
            self.jan1.ui.label_13.setText(self.sorteio[4][1])
            self.jan1.show()
        elif self.ui.radioButton_3.isChecked():
            self.jan2.ui.label_9.setText(self.sorteio[0][1])
            self.jan2.ui.label_10.setText(self.sorteio[1][1])
            self.jan2.ui.label_11.setText(self.sorteio[2][1])
            self.jan2.ui.label_12.setText(self.sorteio[3][1])
            self.jan2.ui.label_13.setText(self.sorteio[4][1])
            self.jan2.ui.label_19.setText(self.sorteio[5][1])
            self.jan2.ui.label_20.setText(self.sorteio[6][1])
            self.jan2.ui.label_21.setText(self.sorteio[7][1])
            self.jan2.ui.label_22.setText(self.sorteio[8][1])
            self.jan2.ui.label_23.setText(self.sorteio[9][1])
            self.jan2.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = Tela()
    inicio.show()
    # Tela().show()
    sys.exit(app.exec_())
    