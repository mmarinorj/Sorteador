# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from main import *
from top5 import *
from top10 import *
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
import os
from datetime import datetime


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
        self.box = QMessageBox()
        self.error1 = QtMultimedia.QSound("error - antigo.wav")
        
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
            
        elif self.ui.radioButton_4.isChecked()\
            or self.ui.radioButton.isChecked():
            fonte = 'Helvetica'
            try:
                arquivo_pdf = QtWidgets.QFileDialog.getSaveFileName(None, "Exportar Sorteio para PDF", "",
                                                                    "PDF files (*.pdf)")[0]
                doc = canvas.Canvas(arquivo_pdf)
                doc.setPageSize(A4)
                # doc.drawImage('top10tela.png', 0 * mm, -2 * mm, width=215 * mm, height=300 * mm)
                doc.setFillColorRGB(0, 0, 0)
                doc.setFont(fonte, 20)
                doc.drawCentredString(105 * mm, 285 * mm, f'Sorteio realizado em {datetime.now().day}/'
                                                          f'{datetime.now().month}/{datetime.now().year} às'
                                                          f' {datetime.now().hour}:{datetime.now().minute}')
                verti_spc1 = 0
                verti_spc2 = 0
                cont1 = 1
                cont2 = 0
                for l in self.sorteio:
                    doc.setFont(fonte, 13)
                    cont2 += 1
                    if cont2 < 51:
                        verti_spc1 += 5.2
                        doc.drawString(7 * mm, (280 - verti_spc1) * mm, f"{cont1}. {l[1]} ({l[0]})")
                        cont1 += 1
                    elif 50 < cont2 < 101:
                        verti_spc2 += 5.2
                        doc.drawString(112 * mm, (280 - verti_spc2) * mm, f"{cont1}. {l[1]} ({l[0]})")
                        cont1 += 1
                    else:
                        doc.setFont(fonte, 7)
                        doc.drawRightString(205 * mm, 11 * mm, 'SORTEADOR 1.0 | www.github.com/mmarinorj')
                        doc.drawRightString(205 * mm, 8 * mm, '@mmarinorj | contato/PIX: mmarinorj@gmail.com')
                        doc.drawRightString(205 * mm, 5 * mm, 'Estimule o desenvolvimento de mais projetos como este!')
                        doc.showPage()
                        # doc.drawImage('top10tela.png', 0 * mm, -2 * mm, width=215 * mm, height=300 * mm)
                        cont2 = 1
                        verti_spc1 = 0
                        verti_spc2 = 0
                        verti_spc1 += 5.2
                        doc.setFont(fonte, 13)
                        doc.drawString(7 * mm, (280 - verti_spc1) * mm, f"{cont1}. {l[1]} ({l[0]})")
                        cont1 += 1
                        
                doc.setFont(fonte, 7)
                doc.drawRightString(205 * mm, 11 * mm, 'SORTEADOR 1.0 | www.github.com/mmarinorj')
                doc.drawRightString(205 * mm, 8 * mm, '@mmarinorj | contato/PIX: mmarinorj@gmail.com')
                doc.drawRightString(205 * mm, 5 * mm, 'Estimule o desenvolvimento de mais projetos como este!')
                doc.save()
                self.ui.ding1.play()
                self.box.about(self.ui.centralwidget, 'Exportação realizada com sucesso', f'O arquivo de nome:'
                                                                                          f'\n{arquivo_pdf}\nfoi salvo'
                                                                                          f' com sucesso!')
                self.abriroarquivo(arquivo_pdf)
            except:
                self.error1.play()
                self.box.about(self.ui.centralwidget, 'Exportação não realizada...', f'A exportação não foi concluída!')

    def abriroarquivo(self, arquivo):
        self.ui.ding1.play()
        dialog = self.box.question(self.ui.centralwidget, "Exportação realizada com sucesso", "Deseja abrir o arquivo salvo?",
                              self.box.StandardButton.Yes | self.box.StandardButton.No)
        if dialog != 65536:
            os.popen(arquivo)
    
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    inicio = Tela()
    inicio.show()
    sys.exit(app.exec_())
    