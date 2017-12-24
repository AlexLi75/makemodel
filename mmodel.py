#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mmebel.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

# ver 0.4 сшивка с объектом отрисовки модел

from PyQt5 import QtCore, QtGui, QtWidgets
import models

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 376, 516))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.label_2.setText("Модель:")

        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("box")
        self.comboBox.addItem("smallbox")
        # self.comboBox.addItem("")
        # self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setText('Ширина:')
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText('100')
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Высота:")

        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText('100')
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setText('Глубина:')
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setText('100')
        self.horizontalLayout_4.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.label_5.setText("Толщина материала:")

        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("6")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.label_7.setText("Зазор:")

        self.horizontalLayout_8.addWidget(self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("0.2")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.label_6.setText("Тип соединения:")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Без сединения")
        self.comboBox_2.addItem("Шип")
        self.comboBox_2.addItem("Болт")
        self.comboBox_2.addItem("Болт+шип")
        self.horizontalLayout_6.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setText("Сгенерить чертёж")
        self.pushButton.clicked.connect(self.makemodel)

        self.verticalLayout.addWidget(self.pushButton)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_7.addWidget(self.groupBox)
        self.groupBox.raise_()
        self.label_7.raise_()
        self.lineEdit_5.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Модель:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Стульчик"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Табурет"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Коробка"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Ящик"))
        self.label.setText(_translate("MainWindow", "ширина:"))
        self.lineEdit.setText(_translate("MainWindow", "100"))
        self.label_3.setText(_translate("MainWindow", "высота:"))
        self.lineEdit_2.setText(_translate("MainWindow", "100"))
        self.label_4.setText(_translate("MainWindow", "длинна:"))
        self.lineEdit_3.setText(_translate("MainWindow", "100"))
        self.label_5.setText(_translate("MainWindow", "материал:"))
        self.lineEdit_4.setText(_translate("MainWindow", "10"))
        self.label_7.setText(_translate("MainWindow", "Зазор:"))
        self.lineEdit_5.setText(_translate("MainWindow", "0.2"))
        self.label_6.setText(_translate("MainWindow", "Вариант соединения:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "болт"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "шип"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "шип+болт"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.clicked.connect(self.makemodel)

        self.groupBox.setTitle(_translate("MainWindow", "предспомтотр"))
    def makemodel(self):
        ## makepanel
        #proverka() # проврка полей на допустимые символы и значени


        drawfig = models.drawmodel() # создаём объект
        drawfig.model = self.comboBox.currentText()
        drawfig.width = float(self.lineEdit.text()) #путь для сохранения
        drawfig.height = float(self.lineEdit_2.text()) #номер заказа
        drawfig.deep = float(self.lineEdit_3.text()) # ширина панели
        drawfig.thinkness = float(self.lineEdit_4.text()) # высота панели
        drawfig.clearance = float(self.lineEdit_5.text()) # номер рисунка
        drawfig.typecon = self.comboBox_2.currentText() # номер рисунка

        drawfig.drawfigure() #отрисовать



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
