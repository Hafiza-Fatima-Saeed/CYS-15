# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cosmetic_billing.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 532)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addToCartBtn = QPushButton(self.centralwidget)
        self.addToCartBtn.setObjectName(u"addToCartBtn")

        self.horizontalLayout.addWidget(self.addToCartBtn)

        self.quantitySpinBox = QSpinBox(self.centralwidget)
        self.quantitySpinBox.setObjectName(u"quantitySpinBox")

        self.horizontalLayout.addWidget(self.quantitySpinBox)

        self.productComboBox = QComboBox(self.centralwidget)
        self.productComboBox.setObjectName(u"productComboBox")

        self.horizontalLayout.addWidget(self.productComboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.cartTable = QTableWidget(self.centralwidget)
        self.cartTable.setObjectName(u"cartTable")

        self.verticalLayout.addWidget(self.cartTable)

        self.billDisplay = QTextEdit(self.centralwidget)
        self.billDisplay.setObjectName(u"billDisplay")

        self.verticalLayout.addWidget(self.billDisplay)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.subtotalLabel = QLabel(self.centralwidget)
        self.subtotalLabel.setObjectName(u"subtotalLabel")

        self.horizontalLayout_2.addWidget(self.subtotalLabel)

        self.totalLabel = QLabel(self.centralwidget)
        self.totalLabel.setObjectName(u"totalLabel")

        self.horizontalLayout_2.addWidget(self.totalLabel)

        self.generateBillBtn = QPushButton(self.centralwidget)
        self.generateBillBtn.setObjectName(u"generateBillBtn")

        self.horizontalLayout_2.addWidget(self.generateBillBtn)

        self.clearCartBtn = QPushButton(self.centralwidget)
        self.clearCartBtn.setObjectName(u"clearCartBtn")

        self.horizontalLayout_2.addWidget(self.clearCartBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 954, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.addToCartBtn.setText(QCoreApplication.translate("MainWindow", u"Add to Cart", None))
        self.subtotalLabel.setText(QCoreApplication.translate("MainWindow", u"            Subtotal: Rs. 0.00", None))
        self.totalLabel.setText(QCoreApplication.translate("MainWindow", u"          Grand Total: Rs: 0.00", None))
        self.generateBillBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Bill", None))
        self.clearCartBtn.setText(QCoreApplication.translate("MainWindow", u"Clear Cart", None))
    

