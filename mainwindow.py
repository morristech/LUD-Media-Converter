# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Dec 10 06:06:38 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(896, 496)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/penguin.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.selectFileButton = QtGui.QPushButton(self.centralwidget)
        self.selectFileButton.setGeometry(QtCore.QRect(40, 90, 151, 41))
        self.selectFileButton.setObjectName(_fromUtf8("selectFileButton"))
        self.statusLabel = QtGui.QLabel(self.centralwidget)
        self.statusLabel.setGeometry(QtCore.QRect(10, 180, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.convertButton = QtGui.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(200, 90, 181, 41))
        self.convertButton.setObjectName(_fromUtf8("convertButton"))
        self.outputFormatGroupBox = QtGui.QGroupBox(self.centralwidget)
        self.outputFormatGroupBox.setEnabled(True)
        self.outputFormatGroupBox.setGeometry(QtCore.QRect(420, 30, 461, 171))
        self.outputFormatGroupBox.setFlat(False)
        self.outputFormatGroupBox.setCheckable(False)
        self.outputFormatGroupBox.setObjectName(_fromUtf8("outputFormatGroupBox"))
        self.androidHDRadioButton = QtGui.QRadioButton(self.outputFormatGroupBox)
        self.androidHDRadioButton.setGeometry(QtCore.QRect(20, 30, 341, 21))
        self.androidHDRadioButton.setObjectName(_fromUtf8("androidHDRadioButton"))
        self.androidQHDRadioButton = QtGui.QRadioButton(self.outputFormatGroupBox)
        self.androidQHDRadioButton.setGeometry(QtCore.QRect(20, 60, 361, 21))
        self.androidQHDRadioButton.setObjectName(_fromUtf8("androidQHDRadioButton"))
        self.appleHDRadioButton = QtGui.QRadioButton(self.outputFormatGroupBox)
        self.appleHDRadioButton.setGeometry(QtCore.QRect(20, 90, 361, 21))
        self.appleHDRadioButton.setObjectName(_fromUtf8("appleHDRadioButton"))
        self.appleFullHDRadioButton = QtGui.QRadioButton(self.outputFormatGroupBox)
        self.appleFullHDRadioButton.setGeometry(QtCore.QRect(20, 120, 441, 21))
        self.appleFullHDRadioButton.setObjectName(_fromUtf8("appleFullHDRadioButton"))
        self.statusLabel_2 = QtGui.QLabel(self.centralwidget)
        self.statusLabel_2.setGeometry(QtCore.QRect(10, 210, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.statusLabel_2.setFont(font)
        self.statusLabel_2.setObjectName(_fromUtf8("statusLabel_2"))
        self.fileName = QtGui.QLabel(self.centralwidget)
        self.fileName.setGeometry(QtCore.QRect(120, 180, 761, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.fileName.setFont(font)
        self.fileName.setObjectName(_fromUtf8("fileName"))
        self.outputFormat = QtGui.QLabel(self.centralwidget)
        self.outputFormat.setGeometry(QtCore.QRect(160, 210, 211, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier 10 Pitch"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.outputFormat.setFont(font)
        self.outputFormat.setObjectName(_fromUtf8("outputFormat"))
        self.imageLabel1 = QtGui.QLabel(self.centralwidget)
        self.imageLabel1.setGeometry(QtCore.QRect(450, 230, 201, 81))
        self.imageLabel1.setObjectName(_fromUtf8("imageLabel1"))
        self.imageLabel2 = QtGui.QLabel(self.centralwidget)
        self.imageLabel2.setGeometry(QtCore.QRect(670, 210, 211, 101))
        self.imageLabel2.setObjectName(_fromUtf8("imageLabel2"))
        self.statusText = QtGui.QLabel(self.centralwidget)
        self.statusText.setGeometry(QtCore.QRect(130, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cantarell"))
        font.setPointSize(12)
        font.setItalic(True)
        self.statusText.setFont(font)
        self.statusText.setObjectName(_fromUtf8("statusText"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 330, 781, 141))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LUD Media Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Welcome to LUD Media Converter", None, QtGui.QApplication.UnicodeUTF8))
        self.selectFileButton.setText(QtGui.QApplication.translate("MainWindow", "Select Media File", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("MainWindow", "File Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.convertButton.setText(QtGui.QApplication.translate("MainWindow", "Convert", None, QtGui.QApplication.UnicodeUTF8))
        self.outputFormatGroupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Output Format", None, QtGui.QApplication.UnicodeUTF8))
        self.androidHDRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Android HD (Galaxy Note 2, S3, Transformer)", None, QtGui.QApplication.UnicodeUTF8))
        self.androidQHDRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Android qHD (HTC Sensation, Galaxy S2)", None, QtGui.QApplication.UnicodeUTF8))
        self.appleHDRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Apple HD (iPhone 4, iPhone 4S)", None, QtGui.QApplication.UnicodeUTF8))
        self.appleFullHDRadioButton.setText(QtGui.QApplication.translate("MainWindow", "Apple Full HD (iPhone 5, iPad2, iPad 3, iPad 4, iPad Mini)", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel_2.setText(QtGui.QApplication.translate("MainWindow", "Output Format:", None, QtGui.QApplication.UnicodeUTF8))
        self.fileName.setText(QtGui.QApplication.translate("MainWindow", "File Name", None, QtGui.QApplication.UnicodeUTF8))
        self.outputFormat.setText(QtGui.QApplication.translate("MainWindow", "Output Format", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel1.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel2.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.statusText.setText(QtGui.QApplication.translate("MainWindow", "Conversion Status", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
