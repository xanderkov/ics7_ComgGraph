# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 670))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 1020))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_15.addWidget(self.label_2)
        self.radioButtonWhite_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonWhite_bg.setChecked(True)
        self.radioButtonWhite_bg.setObjectName("radioButtonWhite_bg")
        self.verticalLayout_15.addWidget(self.radioButtonWhite_bg)
        self.radioButtonBlack_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonBlack_bg.setObjectName("radioButtonBlack_bg")
        self.verticalLayout_15.addWidget(self.radioButtonBlack_bg)
        self.radioButtonYellow_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonYellow_bg.setObjectName("radioButtonYellow_bg")
        self.verticalLayout_15.addWidget(self.radioButtonYellow_bg)
        self.radioButtonGreen_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonGreen_bg.setObjectName("radioButtonGreen_bg")
        self.verticalLayout_15.addWidget(self.radioButtonGreen_bg)
        self.radioButtonRed_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonRed_bg.setObjectName("radioButtonRed_bg")
        self.verticalLayout_15.addWidget(self.radioButtonRed_bg)
        self.radioButtonBlue_bg = QtWidgets.QRadioButton(self.widget_2)
        self.radioButtonBlue_bg.setObjectName("radioButtonBlue_bg")
        self.verticalLayout_15.addWidget(self.radioButtonBlue_bg)
        self.horizontalLayout.addWidget(self.widget_2)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.radioButtonParam = QtWidgets.QRadioButton(self.widget_4)
        self.radioButtonParam.setObjectName("radioButtonParam")
        self.verticalLayout_3.addWidget(self.radioButtonParam)
        self.radioButtonMidPoint = QtWidgets.QRadioButton(self.widget_4)
        self.radioButtonMidPoint.setObjectName("radioButtonMidPoint")
        self.verticalLayout_3.addWidget(self.radioButtonMidPoint)
        self.radioButtonBres = QtWidgets.QRadioButton(self.widget_4)
        self.radioButtonBres.setObjectName("radioButtonBres")
        self.verticalLayout_3.addWidget(self.radioButtonBres)
        self.radioButtonCanon = QtWidgets.QRadioButton(self.widget_4)
        self.radioButtonCanon.setChecked(True)
        self.radioButtonCanon.setObjectName("radioButtonCanon")
        self.verticalLayout_3.addWidget(self.radioButtonCanon)
        self.radioButtonLib = QtWidgets.QRadioButton(self.widget_4)
        self.radioButtonLib.setObjectName("radioButtonLib")
        self.verticalLayout_3.addWidget(self.radioButtonLib)
        self.horizontalLayout.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.radioButtonBlack_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonBlack_line.setChecked(True)
        self.radioButtonBlack_line.setObjectName("radioButtonBlack_line")
        self.verticalLayout_2.addWidget(self.radioButtonBlack_line)
        self.radioButtonWhite_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonWhite_line.setChecked(False)
        self.radioButtonWhite_line.setObjectName("radioButtonWhite_line")
        self.verticalLayout_2.addWidget(self.radioButtonWhite_line)
        self.radioButtonYellow_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonYellow_line.setObjectName("radioButtonYellow_line")
        self.verticalLayout_2.addWidget(self.radioButtonYellow_line)
        self.radioButtonGreen_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonGreen_line.setObjectName("radioButtonGreen_line")
        self.verticalLayout_2.addWidget(self.radioButtonGreen_line)
        self.radioButtonRed_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonRed_line.setObjectName("radioButtonRed_line")
        self.verticalLayout_2.addWidget(self.radioButtonRed_line)
        self.radioButtonFon_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonFon_line.setChecked(False)
        self.radioButtonFon_line.setObjectName("radioButtonFon_line")
        self.verticalLayout_2.addWidget(self.radioButtonFon_line)
        self.radioButtonBlue_line = QtWidgets.QRadioButton(self.widget_3)
        self.radioButtonBlue_line.setObjectName("radioButtonBlue_line")
        self.verticalLayout_2.addWidget(self.radioButtonBlue_line)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelOneC = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        self.labelOneC.setFont(font)
        self.labelOneC.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelOneC.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelOneC.setScaledContents(False)
        self.labelOneC.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOneC.setObjectName("labelOneC")
        self.verticalLayout_6.addWidget(self.labelOneC)
        self.lineEditcicX = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcicX.setSuffix("")
        self.lineEditcicX.setMaximum(10000.0)
        self.lineEditcicX.setProperty("value", 0.0)
        self.lineEditcicX.setObjectName("lineEditcicX")
        self.verticalLayout_6.addWidget(self.lineEditcicX)
        self.lineEditcicY = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcicY.setSuffix("")
        self.lineEditcicY.setMaximum(100000.0)
        self.lineEditcicY.setProperty("value", 0.0)
        self.lineEditcicY.setObjectName("lineEditcicY")
        self.verticalLayout_6.addWidget(self.lineEditcicY)
        self.lineEditR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditR.setSuffix("")
        self.lineEditR.setMaximum(100000.0)
        self.lineEditR.setProperty("value", 200.0)
        self.lineEditR.setObjectName("lineEditR")
        self.verticalLayout_6.addWidget(self.lineEditR)
        self.pushButton_cic = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cic.setObjectName("pushButton_cic")
        self.verticalLayout_6.addWidget(self.pushButton_cic)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelOneE = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(False)
        self.labelOneE.setFont(font)
        self.labelOneE.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelOneE.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelOneE.setScaledContents(False)
        self.labelOneE.setAlignment(QtCore.Qt.AlignCenter)
        self.labelOneE.setObjectName("labelOneE")
        self.verticalLayout_7.addWidget(self.labelOneE)
        self.lineEditcicX_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcicX_2.setSuffix("")
        self.lineEditcicX_2.setMaximum(10000.0)
        self.lineEditcicX_2.setProperty("value", 0.0)
        self.lineEditcicX_2.setObjectName("lineEditcicX_2")
        self.verticalLayout_7.addWidget(self.lineEditcicX_2)
        self.lineEditcicY_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcicY_2.setSuffix("")
        self.lineEditcicY_2.setMaximum(100000.0)
        self.lineEditcicY_2.setProperty("value", 0.0)
        self.lineEditcicY_2.setObjectName("lineEditcicY_2")
        self.verticalLayout_7.addWidget(self.lineEditcicY_2)
        self.lineEditA = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditA.setSuffix("")
        self.lineEditA.setMaximum(10000.0)
        self.lineEditA.setProperty("value", 100.0)
        self.lineEditA.setObjectName("lineEditA")
        self.verticalLayout_7.addWidget(self.lineEditA)
        self.lineEditB = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditB.setSuffix("")
        self.lineEditB.setMaximum(10000.0)
        self.lineEditB.setProperty("value", 50.0)
        self.lineEditB.setObjectName("lineEditB")
        self.verticalLayout_7.addWidget(self.lineEditB)
        self.pushButtonElips = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonElips.setObjectName("pushButtonElips")
        self.verticalLayout_7.addWidget(self.pushButtonElips)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.lineEditStartR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditStartR.setSuffix("")
        self.lineEditStartR.setMaximum(100000.0)
        self.lineEditStartR.setProperty("value", 10.0)
        self.lineEditStartR.setObjectName("lineEditStartR")
        self.verticalLayout_8.addWidget(self.lineEditStartR)
        self.lineEditshagR = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditshagR.setSuffix("")
        self.lineEditshagR.setMaximum(100000.0)
        self.lineEditshagR.setProperty("value", 10.0)
        self.lineEditshagR.setObjectName("lineEditshagR")
        self.verticalLayout_8.addWidget(self.lineEditshagR)
        self.lineEditcount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcount.setSuffix("")
        self.lineEditcount.setMaximum(100000.0)
        self.lineEditcount.setProperty("value", 25.0)
        self.lineEditcount.setObjectName("lineEditcount")
        self.verticalLayout_8.addWidget(self.lineEditcount)
        self.pushButtoncicAll = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtoncicAll.setFont(font)
        self.pushButtoncicAll.setObjectName("pushButtoncicAll")
        self.verticalLayout_8.addWidget(self.pushButtoncicAll)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.lineEditEndR_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditEndR_2.setSuffix("")
        self.lineEditEndR_2.setMaximum(100000.0)
        self.lineEditEndR_2.setProperty("value", 10.0)
        self.lineEditEndR_2.setObjectName("lineEditEndR_2")
        self.verticalLayout_9.addWidget(self.lineEditEndR_2)
        self.lineEditStartR_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditStartR_2.setSuffix("")
        self.lineEditStartR_2.setMaximum(100000.0)
        self.lineEditStartR_2.setProperty("value", 30.0)
        self.lineEditStartR_2.setObjectName("lineEditStartR_2")
        self.verticalLayout_9.addWidget(self.lineEditStartR_2)
        self.lineEditshagR_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditshagR_2.setSuffix("")
        self.lineEditshagR_2.setMaximum(100000.0)
        self.lineEditshagR_2.setProperty("value", 10.0)
        self.lineEditshagR_2.setObjectName("lineEditshagR_2")
        self.verticalLayout_9.addWidget(self.lineEditshagR_2)
        self.lineEditcount_2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineEditcount_2.setSuffix("")
        self.lineEditcount_2.setMaximum(100000.0)
        self.lineEditcount_2.setProperty("value", 25.0)
        self.lineEditcount_2.setObjectName("lineEditcount_2")
        self.verticalLayout_9.addWidget(self.lineEditcount_2)
        self.pushButtonElips_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButtonElips_all.setFont(font)
        self.pushButtonElips_all.setObjectName("pushButtonElips_all")
        self.verticalLayout_9.addWidget(self.pushButtonElips_all)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_time_all_c = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_time_all_c.setFont(font)
        self.pushButton_time_all_c.setObjectName("pushButton_time_all_c")
        self.horizontalLayout_5.addWidget(self.pushButton_time_all_c)
        self.pushButton_time_all_e = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_time_all_e.setFont(font)
        self.pushButton_time_all_e.setObjectName("pushButton_time_all_e")
        self.horizontalLayout_5.addWidget(self.pushButton_time_all_e)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_clean = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clean.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton_clean.setFont(font)
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.verticalLayout.addWidget(self.pushButton_clean)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.addWidget(self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Цвет фона"))
        self.radioButtonWhite_bg.setText(_translate("MainWindow", "Белый"))
        self.radioButtonBlack_bg.setText(_translate("MainWindow", "Черный"))
        self.radioButtonYellow_bg.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_bg.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonRed_bg.setText(_translate("MainWindow", "Красный"))
        self.radioButtonBlue_bg.setText(_translate("MainWindow", "Синий"))
        self.label_4.setText(_translate("MainWindow", "Алгоритмы"))
        self.radioButtonParam.setText(_translate("MainWindow", "Параметрического уравнения"))
        self.radioButtonMidPoint.setText(_translate("MainWindow", "Алгоритма средней точки"))
        self.radioButtonBres.setText(_translate("MainWindow", "Алгоритма Брезенхема "))
        self.radioButtonCanon.setText(_translate("MainWindow", "Канонического уравнения"))
        self.radioButtonLib.setText(_translate("MainWindow", "Библиотечная функция"))
        self.label_3.setText(_translate("MainWindow", "Цвет линии"))
        self.radioButtonBlack_line.setText(_translate("MainWindow", "Черный"))
        self.radioButtonWhite_line.setText(_translate("MainWindow", "Белый"))
        self.radioButtonYellow_line.setText(_translate("MainWindow", "Желтый"))
        self.radioButtonGreen_line.setText(_translate("MainWindow", "Зеленый"))
        self.radioButtonRed_line.setText(_translate("MainWindow", "Красный"))
        self.radioButtonFon_line.setText(_translate("MainWindow", "Цвет фона"))
        self.radioButtonBlue_line.setText(_translate("MainWindow", "Синий"))
        self.labelOneC.setText(_translate("MainWindow", "Одна окружность. Коорд. центра"))
        self.lineEditcicX.setPrefix(_translate("MainWindow", "X: "))
        self.lineEditcicY.setPrefix(_translate("MainWindow", "Y:"))
        self.lineEditR.setPrefix(_translate("MainWindow", "R: "))
        self.pushButton_cic.setText(_translate("MainWindow", "Построить окружность"))
        self.labelOneE.setText(_translate("MainWindow", "Один эллипс. Коорд. Центра"))
        self.lineEditcicX_2.setPrefix(_translate("MainWindow", "X: "))
        self.lineEditcicY_2.setPrefix(_translate("MainWindow", "Y:"))
        self.lineEditA.setPrefix(_translate("MainWindow", "Ширина: "))
        self.lineEditB.setPrefix(_translate("MainWindow", "Высота: "))
        self.pushButtonElips.setText(_translate("MainWindow", "Построить эллипс"))
        self.label.setText(_translate("MainWindow", "Спектр окружностей \n"
" Кординаты центра выше"))
        self.lineEditStartR.setPrefix(_translate("MainWindow", "Начальный радиус: "))
        self.lineEditshagR.setPrefix(_translate("MainWindow", "Шаг изменения: "))
        self.lineEditcount.setPrefix(_translate("MainWindow", "количество окруж.: "))
        self.pushButtoncicAll.setText(_translate("MainWindow", "Построить спектр окр."))
        self.label_5.setText(_translate("MainWindow", "Спектр эллипсов \n"
" Координаты центра выше"))
        self.lineEditEndR_2.setPrefix(_translate("MainWindow", "Начальная высота:  "))
        self.lineEditStartR_2.setPrefix(_translate("MainWindow", "Начальная ширина:  "))
        self.lineEditshagR_2.setPrefix(_translate("MainWindow", "Шаг изменения: "))
        self.lineEditcount_2.setPrefix(_translate("MainWindow", "Количество: "))
        self.pushButtonElips_all.setText(_translate("MainWindow", "Построить спектр эллипсов"))
        self.pushButton_time_all_c.setText(_translate("MainWindow", "Сравнение времени \n"
"построение окружности"))
        self.pushButton_time_all_e.setText(_translate("MainWindow", "Сравнение времени \n"
"построение эллипса"))
        self.pushButton_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.menu.setTitle(_translate("MainWindow", "Справка"))
        self.action.setText(_translate("MainWindow", "О программе"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
