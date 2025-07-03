# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Input.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SortingApp(object):
    def setupUi(self, SortingApp):
        if not SortingApp.objectName():
            SortingApp.setObjectName(u"SortingApp")
        SortingApp.resize(743, 649)
        self.centralwidget = QWidget(SortingApp)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_layout = QHBoxLayout(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.left_layout = QVBoxLayout()
        self.left_layout.setObjectName(u"left_layout")
        self.mode_layout = QHBoxLayout()
        self.mode_layout.setObjectName(u"mode_layout")
        self.compare_two_radio = QRadioButton(self.centralwidget)
        self.compare_two_radio.setObjectName(u"compare_two_radio")

        self.mode_layout.addWidget(self.compare_two_radio)

        self.compare_async_radio = QRadioButton(self.centralwidget)
        self.compare_async_radio.setObjectName(u"compare_async_radio")

        self.mode_layout.addWidget(self.compare_async_radio)


        self.left_layout.addLayout(self.mode_layout)

        self.algo_compare_async_layout = QVBoxLayout()
        self.algo_compare_async_layout.setObjectName(u"algo_compare_async_layout")
        self.algo_async_label = QLabel(self.centralwidget)
        self.algo_async_label.setObjectName(u"algo_async_label")

        self.algo_compare_async_layout.addWidget(self.algo_async_label)

        self.algo_async_combo = QComboBox(self.centralwidget)
        self.algo_async_combo.setObjectName(u"algo_async_combo")
        self.algo_async_combo.setEnabled(False)

        self.algo_compare_async_layout.addWidget(self.algo_async_combo)

        self.asymptotic_label = QLabel(self.centralwidget)
        self.asymptotic_label.setObjectName(u"asymptotic_label")

        self.algo_compare_async_layout.addWidget(self.asymptotic_label)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")

        self.algo_compare_async_layout.addWidget(self.comboBox)


        self.left_layout.addLayout(self.algo_compare_async_layout)

        self.algo_compare_two_layout = QVBoxLayout()
        self.algo_compare_two_layout.setObjectName(u"algo_compare_two_layout")
        self.algo1_label = QLabel(self.centralwidget)
        self.algo1_label.setObjectName(u"algo1_label")

        self.algo_compare_two_layout.addWidget(self.algo1_label)

        self.algo1_combo = QComboBox(self.centralwidget)
        self.algo1_combo.setObjectName(u"algo1_combo")
        self.algo1_combo.setEnabled(False)

        self.algo_compare_two_layout.addWidget(self.algo1_combo)

        self.algo2_label = QLabel(self.centralwidget)
        self.algo2_label.setObjectName(u"algo2_label")

        self.algo_compare_two_layout.addWidget(self.algo2_label)

        self.algo2_combo = QComboBox(self.centralwidget)
        self.algo2_combo.setObjectName(u"algo2_combo")
        self.algo2_combo.setEnabled(False)

        self.algo_compare_two_layout.addWidget(self.algo2_combo)


        self.left_layout.addLayout(self.algo_compare_two_layout)

        self.graph_widget = QWidget(self.centralwidget)
        self.graph_widget.setObjectName(u"graph_widget")
        self.graph_widget.setMinimumSize(QSize(400, 300))

        self.left_layout.addWidget(self.graph_widget)


        self.main_layout.addLayout(self.left_layout)

        self.right_layout = QVBoxLayout()
        self.right_layout.setObjectName(u"right_layout")
        self.csv_layout = QVBoxLayout()
        self.csv_layout.setObjectName(u"csv_layout")
        self.csv_row = QHBoxLayout()
        self.csv_row.setObjectName(u"csv_row")
        self.csv_checkbox = QCheckBox(self.centralwidget)
        self.csv_checkbox.setObjectName(u"csv_checkbox")

        self.csv_row.addWidget(self.csv_checkbox)

        self.load_button = QPushButton(self.centralwidget)
        self.load_button.setObjectName(u"load_button")
        self.load_button.setEnabled(False)

        self.csv_row.addWidget(self.load_button)


        self.csv_layout.addLayout(self.csv_row)


        self.right_layout.addLayout(self.csv_layout)

        self.data_type_layout = QVBoxLayout()
        self.data_type_layout.setObjectName(u"data_type_layout")
        self.data_type_layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.data_type_label = QLabel(self.centralwidget)
        self.data_type_label.setObjectName(u"data_type_label")

        self.data_type_layout.addWidget(self.data_type_label)

        self.data_type_combo = QComboBox(self.centralwidget)
        self.data_type_combo.setObjectName(u"data_type_combo")

        self.data_type_layout.addWidget(self.data_type_combo)


        self.right_layout.addLayout(self.data_type_layout)

        self.plot_button = QPushButton(self.centralwidget)
        self.plot_button.setObjectName(u"plot_button")
        self.plot_button.setEnabled(False)

        self.right_layout.addWidget(self.plot_button)


        self.main_layout.addLayout(self.right_layout)

        SortingApp.setCentralWidget(self.centralwidget)

        self.retranslateUi(SortingApp)

        QMetaObject.connectSlotsByName(SortingApp)
    # setupUi

    def retranslateUi(self, SortingApp):
        SortingApp.setWindowTitle(QCoreApplication.translate("SortingApp", u"Sorting Algorithm Analyzer", None))
        self.centralwidget.setStyleSheet(QCoreApplication.translate("SortingApp", u"background-color: rgb(0, 0, 79);", None))
        self.compare_two_radio.setStyleSheet(QCoreApplication.translate("SortingApp", u"color: white; font-size: 16px; font-family: 'Century Gothic'; font-weight: bold;", None))
        self.compare_two_radio.setText(QCoreApplication.translate("SortingApp", u"Compare Two Algorithms", None))
        self.compare_async_radio.setStyleSheet(QCoreApplication.translate("SortingApp", u"color: white; font-size: 16px; font-family: 'Century Gothic'; font-weight: bold;", None))
        self.compare_async_radio.setText(QCoreApplication.translate("SortingApp", u"Compare with Asymptotic Efficiency", None))
        self.algo_async_label.setText(QCoreApplication.translate("SortingApp", u"Algorithm:", None))
        self.algo_async_combo.setStyleSheet(QCoreApplication.translate("SortingApp", u"QComboBox { background-color: white; border: 2px solid rgb(0, 0, 79); color: rgb(0, 0, 79); padding: 5px; font-size: 12px; }", None))
        self.asymptotic_label.setText(QCoreApplication.translate("SortingApp", u"Asymptotic Efficiency:", None))
        self.algo1_label.setText(QCoreApplication.translate("SortingApp", u"Algorithm 1:", None))
        self.algo1_combo.setStyleSheet(QCoreApplication.translate("SortingApp", u"QComboBox { background-color: white; border: 2px solid rgb(0, 0, 79); color: rgb(0, 0, 79); padding: 5px; font-size: 12px; }", None))
        self.algo2_label.setText(QCoreApplication.translate("SortingApp", u"Algorithm 2:", None))
        self.algo2_combo.setStyleSheet(QCoreApplication.translate("SortingApp", u"QComboBox { background-color: white; border: 2px solid rgb(0, 0, 79); color: rgb(0, 0, 79); padding: 5px; font-size: 12px; }", None))
        self.graph_widget.setStyleSheet(QCoreApplication.translate("SortingApp", u"background-color: white; border: 2px solid rgb(0, 0, 79);", None))
        self.csv_checkbox.setText(QCoreApplication.translate("SortingApp", u"Use CSV Data", None))
        self.load_button.setStyleSheet(QCoreApplication.translate("SortingApp", u"QPushButton:disabled { background-color: #d3d3d3; color: #a9a9a9; border: 1px solid #a9a9a9; } QPushButton:enabled { background-color: rgb(0, 0, 79); color: white; font-size: 16px; }", None))
        self.load_button.setText(QCoreApplication.translate("SortingApp", u"Load CSV", None))
        self.data_type_label.setText(QCoreApplication.translate("SortingApp", u"Data Type:", None))
        self.data_type_combo.setStyleSheet(QCoreApplication.translate("SortingApp", u"QComboBox { background-color: white; border: 2px solid rgb(0, 0, 79); color: rgb(0, 0, 79); padding: 5px; font-size: 12px; }", None))
        self.plot_button.setStyleSheet(QCoreApplication.translate("SortingApp", u"background-color: white; color: rgb(0, 0, 79); font-size: 16px;", None))
        self.plot_button.setText(QCoreApplication.translate("SortingApp", u"Plot Graph", None))
    # retranslateUi

