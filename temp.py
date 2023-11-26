
import random
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
from datetime import datetime, date
# lista = [[2104, "Marcelo Marino"], [1107, "Ricardo Argueles"]]
# print(lista)
# temp = random.choice(lista)
# lista.remove(temp)
# print(lista)
# temp = random.choice(lista)
# lista.remove(temp)
# print(lista)
# sorteio = [['Bloco', 'Unidade', 'Etapa1', 'Etapa2'], ['1', '101', 'S 69', ''], ['1', '102', 'S 59', ''],
#          ['1', '103', 'S 73', ''], ['1', '104', 'S 60', ''], ['1', '105', 'S 52', ''], ['1', '106', 'S 26', ''],
#          ['1', '107', 'S 79', ''], ['1', '108', 'S 72', ''], ['1', '201', 'S 49', ''], ['1', '202', 'S 65', 'A 15'],
#          ['1', '203', 'S 76', ''], ['1', '204', 'S 71', ''], ['1', '205', 'S 58', ''], ['1', '206', 'S 77', ''],
#          ['1', '207', 'S 30', ''], ['1', '208', 'S 68', ''], ['1', '301', 'S 84', ''], ['1', '302', 'S 64', 'A 20'],
#          ['1', '303', 'S 63', 'A 16'], ['1', '304', 'S 62', ''], ['1', '305', 'S 81', ''], ['1', '306', 'S 19', ''],
#          ['1', '307', 'S 11', ''], ['1', '308', 'S 67', ''], ['1', '401', 'S 70', ''], ['1', '402', 'S 53', 'A 17'],
#          ['1', '403', 'S 46', 'A 19'], ['1', '404', 'S 45', ''], ['1', '405', 'S 48', ''], ['1', '406', 'S 75', ''],
#          ['1', '407', 'S 78', ''], ['1', '408', 'S 51', ''], ['1', '501', 'S 87', ''], ['1', '502', 'S 21', 'A 18'],
#          ['1', '503', 'S 50', 'A 21'], ['1', '504', 'S 47', ''], ['1', '505', 'S 01', ''], ['1', '506', 'S 25', ''],
#          ['1', '507', 'S 80', ''], ['1', '508', 'S 22', ''], ['1', '601', 'S 61', ''], ['1', '602', 'S 55', 'A 23'],
#          ['1', '603', 'S 54', 'A 22'], ['1', '604', 'S 17', ''], ['1', '605', 'S 82', ''], ['1', '606', 'S 32', ''],
#          ['1', '607', 'S 74', ''], ['1', '608', 'S 56', ''], ['1', '701', 'S 20', 'A 27'], ['1', '702', 'S 23', 'A 31'],
#          ['1', '703', 'S 86', 'A 26'], ['1', '704', 'S 18', 'A 28'], ['1', '705', 'S 66', 'A 24'],
#          ['1', '706', 'S 85', 'A 30'], ['1', '707', 'S 57', 'A 25'], ['1', '708', 'S 83', 'A 29'],
#          ['2', '101', 'S 14', 'A 39'], ['2', '102', 'S 15', 'A 06'], ['2', '103', 'S 44', 'A 02'],
#          ['2', '104', 'S 42', 'A 04'], ['2', '201', 'S 36', 'A 07'], ['2', '202', 'S 37', 'A 03'],
#          ['2', '203', 'S 12', 'A 38'], ['2', '204', 'S 27', 'A 09'], ['2', '301', 'S 09', 'A 14'],
#          ['2', '302', 'S 38', 'A 01'], ['2', '303', 'S 41', 'A 08'], ['2', '304', 'S 06', 'A 13'],
#          ['2', '401', 'S 28', 'A 12'], ['2', '402', 'S 08', 'A 10'], ['2', '403', 'S 39', 'A 11'],
#          ['2', '404', 'S 03', 'A 05'], ['2', '501', 'S 13', 'A 35'], ['2', '502', 'S 04', 'A 41'],
#          ['2', '503', 'S 07', 'A 40'], ['2', '504', 'S 43', 'A 34'], ['2', '601', 'S 16', 'A 37'],
#          ['2', '602', 'S 05', 'S 35'], ['2', '603', 'S 02', 'A 42'], ['2', '604', 'S 40', 'S 34'],
#          ['2', '701', 'S 29', 'A 32'], ['2', '702', 'S 10', 'A 33'], ['2', '703', 'S 24', 'S 33'],
#          ['2', '704', 'S 31', 'A 36']]
# ding1 = QtMultimedia.QSound("ding - antigo.wav")
# error1 = QtMultimedia.QSound("error - antigo.wav")
# box = QtWidgets.QMessageBox()
# try:
#     arquivo_pdf = QtWidgets.QFileDialog.getSaveFileName(None, "Exportar Sorteio para PDF", "",
#                                                         "PDF files (*.pdf)")[0]
#     doc = canvas.Canvas(arquivo_pdf)
#     doc.setPageSize(A4)
#     doc.drawImage(0 * mm, -2 * mm, width=215 * mm, height=300 * mm)
#     doc.setFillColorRGB(1, 1, 1)
#     doc.setFont('Helvetica', 8)
#     doc.drawCentredString(105 * mm, 270 * mm, f'Sorteio realizado em {datetime.today()}')
#     verti_spc = 0
#     for l in sorteio[0:57]:
#         doc.setFont('Helvetica', 9)
#         verti_spc += 4.3
#         horiz_spc = 0
#         for c in l:
#             horiz_spc += 20
#             doc.drawCentredString(horiz_spc * mm, (265 - verti_spc) * mm, c)
#         doc.setFont('Helvetica', 8.5)
#         doc.drawString(15 * mm, (265 - verti_spc - 0.8) * mm, "___________________________________________")
#         doc.drawString(105 * mm, (265 - verti_spc - 0.8) * mm, "|")
#
#     verti_spc = 0
#     for l in sorteio[0:1]:
#         doc.setFont('Helvetica', 9)
#         verti_spc += 4.3
#         horiz_spc = 0
#         for c in l:
#             horiz_spc += 20
#             doc.drawCentredString((105 + horiz_spc) * mm, (265 - verti_spc) * mm, c)
#         doc.setFont('Helvetica', 8.5)
#         doc.drawString(120 * mm, (265 - verti_spc - 0.8) * mm,
#                        "___________________________________________")
#
#     verti_spc = 0
#     for l in sorteio[57:]:
#         doc.setFont('Helvetica', 9)
#         verti_spc += 4.3
#         horiz_spc = 0
#         for c in l:
#             horiz_spc += 20
#             doc.drawCentredString((105 + horiz_spc) * mm, (260.7 - verti_spc) * mm, c)
#         doc.setFont('Helvetica', 8.5)
#         doc.drawString(120 * mm, (260.7 - verti_spc - 0.8) * mm,
#                        "___________________________________________")
#     doc.setFont('Helvetica', 5)
#     doc.drawRightString(205 * mm, 9 * mm, 'Palazzo Imperial Boulevard Rèsidence - Freguesia de Jacarepaguá')
#     doc.drawRightString(205 * mm, 7 * mm, 'SORTEIO PRO VAGAS | contato/PIX: mmarinorj@gmail.com')
#     doc.drawRightString(205 * mm, 5 * mm,
#                         'Dôe para estimular o desenvolvimento de mais projetos como este')
#     doc.save()
#     ding1.play()
#     box.about(Ui_MainWindow, 'Exportação realizada com sucesso',
#                    f'O arquivo de nome:\n{arquivo_pdf}\nfoi salvo com '
#                    f'sucesso!')
#
# except:
#     error1.play()
#     box.about(QMainWindow, 'Exportação não realizada...', f'A exportação não foi concluída!')
#
#
# def abriroarquivo(arquivo):
#     ding1.play()
#     dialog = box.question(QMainWindow, "Exportação realizada com sucesso", "Deseja abrir o arquivo salvo?",
#                                box.StandardButton.Yes | box.StandardButton.No)
#     if dialog != 65536:
#         os.popen(arquivo)

# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
#
# canvas = canvas.Canvas("form.pdf", pagesize=letter)
# canvas.setLineWidth(.3)
# canvas.setFont('Helvetica', 12)
#
# canvas.drawString(30, 750, 'COMUNICADO OFICIAL')
# canvas.drawString(30, 735, 'EMPRESAS ACME')
# canvas.drawString(500, 750, "12/12/2011")
# canvas.line(480, 747, 580, 747)
#
# canvas.drawString(275, 725, 'SALDO DEVEDOR:')
# canvas.drawString(500, 725, "R$ 1.000,00")
# canvas.line(378, 723, 580, 723)
#
# canvas.drawString(30, 703, 'RECEBIDO POR:')
# canvas.line(130, 700, 580, 700)
# canvas.drawString(130, 703, "JOHN DOE")
#
# canvas.save()

import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

doc = SimpleDocTemplate("form_letter.pdf", pagesize=letter,
                        rightMargin=72, leftMargin=72,
                        topMargin=72, bottomMargin=18)
Story = []
logo = "python-logo.png"
magName = "Pythonista"
issueNum = 12
subPrice = "99.00"
limitedDate = "03/05/2010"
freeGift = "Bisão de pelúcia"

formatted_time = time.ctime()
full_name = "Mike Driscoll"
address_parts = ["411 State St.", "Marshalltown, IA 50158"]

# im = Image(logo, 2 * inch, 2 * inch)
# Story.append(im)

# styles = getSampleStyleSheet()
# styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
# ptext = '<font size=12>%s</font>' % formatted_time
#
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
#
# # Create return address
# ptext = '<font size=12>%s</font>' % full_name
# Story.append(Paragraph(ptext, styles["Normal"]))
# for part in address_parts:
#     ptext = '<font size=12>%s</font>' % part.strip()
#     Story.append(Paragraph(ptext, styles["Normal"]))
#
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Caro(a) %s:</font>' % full_name.split()[0].strip()
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
#
# ptext = '<font size=12>Gostaríamos de recebê-lo na nossa base de assinantes da Revista %s! \
#         Você receberá %s edições pelo excelente preço inicial de $%s. Por favor responda até\
#         %s para começar a receber nossa publicação e ainda levar esse maravilhoso presente: %s.</font>' % (magName,
#                                                                                                            issueNum,
#                                                                                                            subPrice,
#                                                                                                            limitedDate,
#                                                                                                            freeGift)
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
#
# ptext = '<font size=12>Agradecemos muito e esperamos seu retorno para lhe servir.</font>'
# Story.append(Paragraph(ptext, styles["Justify"]))
# Story.append(Spacer(1, 12))
# ptext = '<font size=12>Atenciosamente,</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 48))
# ptext = '<font size=12>Ima Sucker</font>'
# Story.append(Paragraph(ptext, styles["Normal"]))
# Story.append(Spacer(1, 12))
# doc.build(Story)

# from reportlab.pdfgen import canvas
#
# report = canvas.Canvas("multiple_pages.pdf")
# report.setFont("Courier", 12)
#
# report.drawString(50, 800, "**This is the first page...**")
# report.showPage()
#
# report.drawString(50, 800, "**This is the second page...**")
# report.showPage()
#
# report.drawString(50, 800, "**This is the third page...**")
# report.showPage()
#
# report.save()

# import PageBreak, along with SimpleDocTemplate
from reportlab.platypus import SimpleDocTemplate, PageBreak

# create new file with image and multiple pages
doc = SimpleDocTemplate("sample_image_multiple_pages.pdf")
info = []

image_file = "1st - ouro.png"

im = Image(image_file, 3 * inch, 3 * inch)
info.append(im)

# add page break
info.append(PageBreak())
info.append(Paragraph("Second page..."))

# add third page
info.append(PageBreak())
info.append(Paragraph("Third page..."))

# build PDF
doc.build(info)
