# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 699)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(170, 30, 161, 121))
        self.groupBox.setObjectName("groupBox")
        self.box_color_segment = QtWidgets.QComboBox(self.groupBox)
        self.box_color_segment.setGeometry(QtCore.QRect(10, 50, 141, 61))
        self.box_color_segment.setObjectName("box_color_segment")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.box_color_segment.addItem("")
        self.graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(590, 0, 750, 700))
        self.graph.setObjectName("graph")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 500, 511, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.table_segments = QtWidgets.QTableWidget(self.groupBox_4)
        self.table_segments.setGeometry(QtCore.QRect(10, 30, 470, 151))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.table_segments.setFont(font)
        self.table_segments.setColumnCount(2)
        self.table_segments.setObjectName("table_segments")
        self.table_segments.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_segments.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_segments.setHorizontalHeaderItem(1, item)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 30, 141, 121))
        self.groupBox_5.setObjectName("groupBox_5")
        self.box_color_cutter = QtWidgets.QComboBox(self.groupBox_5)
        self.box_color_cutter.setGeometry(QtCore.QRect(10, 50, 121, 61))
        self.box_color_cutter.setObjectName("box_color_cutter")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.box_color_cutter.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(340, 30, 231, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.box_color_result = QtWidgets.QComboBox(self.groupBox_2)
        self.box_color_result.setGeometry(QtCore.QRect(10, 50, 211, 61))
        self.box_color_result.setObjectName("box_color_result")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.box_color_result.addItem("")
        self.but_connect_cutter = QtWidgets.QPushButton(self.centralwidget)
        self.but_connect_cutter.setGeometry(QtCore.QRect(290, 220, 291, 61))
        self.but_connect_cutter.setObjectName("but_connect_cutter")
        self.but_cut = QtWidgets.QPushButton(self.centralwidget)
        self.but_cut.setGeometry(QtCore.QRect(20, 360, 261, 61))
        self.but_cut.setObjectName("but_cut")
        self.but_clean = QtWidgets.QPushButton(self.centralwidget)
        self.but_clean.setGeometry(QtCore.QRect(20, 430, 261, 61))
        self.but_clean.setObjectName("but_clean")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 360, 301, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 210, 261, 141))
        self.groupBox_3.setObjectName("groupBox_3")
        self.box_x = QtWidgets.QSpinBox(self.groupBox_3)
        self.box_x.setGeometry(QtCore.QRect(10, 30, 111, 41))
        self.box_x.setMinimum(-10000)
        self.box_x.setMaximum(10000)
        self.box_x.setSingleStep(100)
        self.box_x.setProperty("value", 200)
        self.box_x.setObjectName("box_x")
        self.box_y = QtWidgets.QSpinBox(self.groupBox_3)
        self.box_y.setGeometry(QtCore.QRect(140, 30, 111, 41))
        self.box_y.setMinimum(-10000)
        self.box_y.setMaximum(10000)
        self.box_y.setSingleStep(100)
        self.box_y.setProperty("value", 200)
        self.box_y.setObjectName("box_y")
        self.but_input_point_segment = QtWidgets.QPushButton(self.groupBox_3)
        self.but_input_point_segment.setGeometry(QtCore.QRect(140, 80, 111, 51))
        self.but_input_point_segment.setObjectName("but_input_point_segment")
        self.but_input_point_cutter = QtWidgets.QPushButton(self.groupBox_3)
        self.but_input_point_cutter.setGeometry(QtCore.QRect(10, 80, 111, 51))
        self.but_input_point_cutter.setObjectName("but_input_point_cutter")
        self.table_cutter = QtWidgets.QTableWidget(self.centralwidget)
        self.table_cutter.setGeometry(QtCore.QRect(1190, 1190, 471, 151))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.table_cutter.setFont(font)
        self.table_cutter.setColumnCount(2)
        self.table_cutter.setObjectName("table_cutter")
        self.table_cutter.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_cutter.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_cutter.setHorizontalHeaderItem(1, item)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(1170, 1150, 521, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.but_connect_segment = QtWidgets.QPushButton(self.centralwidget)
        self.but_connect_segment.setGeometry(QtCore.QRect(290, 290, 291, 61))
        self.but_connect_segment.setObjectName("but_connect_segment")
        self.rb_delete = QtWidgets.QRadioButton(self.centralwidget)
        self.rb_delete.setGeometry(QtCore.QRect(20, 150, 421, 61))
        self.rb_delete.setChecked(True)
        self.rb_delete.setObjectName("rb_delete")
        self.groupBox_6.raise_()
        self.groupBox_4.raise_()
        self.groupBox.raise_()
        self.graph.raise_()
        self.groupBox_5.raise_()
        self.groupBox_2.raise_()
        self.but_connect_cutter.raise_()
        self.but_cut.raise_()
        self.but_clean.raise_()
        self.label.raise_()
        self.groupBox_3.raise_()
        self.table_cutter.raise_()
        self.but_connect_segment.raise_()
        self.rb_delete.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Отсечение многоугольников. Алгоритм Сазерленда Ходжмена."))
        self.groupBox.setTitle(_translate("MainWindow", "Цвет \"отсекаемого\""))
        self.box_color_segment.setItemText(0, _translate("MainWindow", "Черный"))
        self.box_color_segment.setItemText(1, _translate("MainWindow", "Синий"))
        self.box_color_segment.setItemText(2, _translate("MainWindow", "Зеленый"))
        self.box_color_segment.setItemText(3, _translate("MainWindow", "Красный"))
        self.box_color_segment.setItemText(4, _translate("MainWindow", "Розовый"))
        self.box_color_segment.setItemText(5, _translate("MainWindow", "Бирюзовый"))
        self.box_color_segment.setItemText(6, _translate("MainWindow", "Голубой"))
        self.box_color_segment.setItemText(7, _translate("MainWindow", "Желтый"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Введенные вершины отсекаемого"))
        item = self.table_segments.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X1"))
        item = self.table_segments.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y1"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Цвет отсекателя"))
        self.box_color_cutter.setItemText(0, _translate("MainWindow", "Красный"))
        self.box_color_cutter.setItemText(1, _translate("MainWindow", "Черный"))
        self.box_color_cutter.setItemText(2, _translate("MainWindow", "Зеленый"))
        self.box_color_cutter.setItemText(3, _translate("MainWindow", "Розовый"))
        self.box_color_cutter.setItemText(4, _translate("MainWindow", "Бирюзовый"))
        self.box_color_cutter.setItemText(5, _translate("MainWindow", "Голубой"))
        self.box_color_cutter.setItemText(6, _translate("MainWindow", "Синий"))
        self.box_color_cutter.setItemText(7, _translate("MainWindow", "Желтый"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Цвет результата"))
        self.box_color_result.setItemText(0, _translate("MainWindow", "Зеленый"))
        self.box_color_result.setItemText(1, _translate("MainWindow", "Черный"))
        self.box_color_result.setItemText(2, _translate("MainWindow", "Розовый"))
        self.box_color_result.setItemText(3, _translate("MainWindow", "Бирюзовый"))
        self.box_color_result.setItemText(4, _translate("MainWindow", "Голубой"))
        self.box_color_result.setItemText(5, _translate("MainWindow", "Красный"))
        self.box_color_result.setItemText(6, _translate("MainWindow", "Синий"))
        self.box_color_result.setItemText(7, _translate("MainWindow", "Желтый"))
        self.but_connect_cutter.setText(_translate("MainWindow", "Замнкнуть отсекатель"))
        self.but_cut.setText(_translate("MainWindow", "Отсечь"))
        self.but_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.label.setText(_translate("MainWindow", "Левая кнопка мыши - ввод вершины отсекаемого;  \n"
" правая - ввод вершины отсекателя.\n"
" При вводе на холсте вершины отсекаемого,\n"
" близкой к прямой,\n"
" проходящей через ребро отсекателя, \n"
" будет введена точка, \n"
" лежащая на этой прямой.  "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Ввод вершины"))
        self.box_x.setPrefix(_translate("MainWindow", "X: "))
        self.box_y.setPrefix(_translate("MainWindow", "Y: "))
        self.but_input_point_segment.setText(_translate("MainWindow", "Отсекаемое"))
        self.but_input_point_cutter.setText(_translate("MainWindow", "Отсекатель"))
        item = self.table_cutter.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X1"))
        item = self.table_cutter.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y1"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Введенные вершины отсекателя"))
        self.but_connect_segment.setText(_translate("MainWindow", "Замнкнуть отсекаемое"))
        self.rb_delete.setText(_translate("MainWindow", "Удалять \"ложные\" ребра"))
