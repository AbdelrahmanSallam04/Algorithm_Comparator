# -*- coding: utf-8 -*-
import random

################################################################################
## Form generated from reading UI file 'Home.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(840, 522)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 79);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 20, 241, 61))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.WelcomeText = QLabel(self.centralwidget)
        self.WelcomeText.setObjectName(u"WelcomeText")
        self.WelcomeText.setGeometry(QRect(80, 70, 671, 61))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(True)
        self.WelcomeText.setFont(font1)
        self.WelcomeText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setEnabled(True)
        self.Start.setGeometry(QRect(90, 240, 191, 61))
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.Start.setFont(font2)
        self.Start.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.Start.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Start.setStyleSheet(u"color: rgb(0, 0, 79);\n"
"background-color: rgb(255, 255, 255);")
        self.Start.setCheckable(False)
        self.Start.setAutoDefault(False)
        self.Start.setFlat(False)
        self.Sortingimg = QLabel(self.centralwidget)
        self.Sortingimg.setObjectName(u"Sortingimg")
        self.Sortingimg.setEnabled(True)
        self.Sortingimg.setGeometry(QRect(330, 150, 461, 251))
        self.Sortingimg.setPixmap(QPixmap(u":/images/Images/Sortings.png"))
        self.Sortingimg.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 840, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Start.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)

        self.welcome_text = "to the Sorting Algorithms comparator :)"
        self.jumbled_text = self.jumble_text(self.welcome_text)
        self.is_sorted = False  # Track if text is sorted or jumbled
        self.current_step = 0
        self.steps = self.generate_rearrangement_steps(self.jumbled_text, self.welcome_text)

        # Timer for the animation
        self.typing_timer = QTimer()
        self.typing_timer.timeout.connect(self.update_text)
        self.typing_timer.start(150)

    def jumble_text(self, text):
        text_list = list(text)
        random.shuffle(text_list)
        return ''.join(text_list)

    def generate_rearrangement_steps(self, jumbled, target):
        steps = [list(jumbled)]
        current = list(jumbled)

        for i in range(len(target)):
            if current[i] != target[i]:
                # Find the target letter's current index
                index_to_swap = current.index(target[i], i)
                current[i], current[index_to_swap] = current[index_to_swap], current[i]
                steps.append(current[:])  # Append a copy of the current state

        return [''.join(step) for step in steps]

    def update_text(self):
        if self.is_sorted:
            # If sorted, jumble the text again and reset for sorting
            self.jumbled_text = self.jumble_text(self.welcome_text)
            self.steps = self.generate_rearrangement_steps(self.jumbled_text, self.welcome_text)
            self.current_step = 0
            self.is_sorted = False
        else:
            # Sort the text step-by-step
            if self.current_step < len(self.steps):
                self.WelcomeText.setText(self.steps[self.current_step])
                self.current_step += 1
            else:
                # Mark as sorted when done
                self.is_sorted = True
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Welcome!", None))
        self.WelcomeText.setText("")
        self.Start.setText(QCoreApplication.translate("MainWindow", u"Let's Get Started!!", None))
        self.Sortingimg.setText("")
    # retranslateUi

