# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(779, 732)
        self.gridLayout = QtWidgets.QGridLayout(Window)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Window)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.dirEdit = QtWidgets.QLineEdit(Window)
        self.dirEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.dirEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.dirEdit.setObjectName("dirEdit")
        self.gridLayout.addWidget(self.dirEdit, 1, 0, 1, 1)
        self.loadFilesButton = QtWidgets.QPushButton(Window)
        self.loadFilesButton.setMinimumSize(QtCore.QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.loadFilesButton.setFont(font)
        self.loadFilesButton.setObjectName("loadFilesButton")
        self.gridLayout.addWidget(self.loadFilesButton, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(Window)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.srcFileList = QtWidgets.QListWidget(self.layoutWidget)
        self.srcFileList.setObjectName("srcFileList")
        self.verticalLayout.addWidget(self.srcFileList)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dstFileList = QtWidgets.QListWidget(self.layoutWidget1)
        self.dstFileList.setObjectName("dstFileList")
        self.verticalLayout_2.addWidget(self.dstFileList)
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(Window)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.formatList = QtWidgets.QComboBox(Window)
        self.formatList.setMinimumSize(QtCore.QSize(0, 30))
        self.formatList.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.formatList.setFont(font)
        self.formatList.setObjectName("formatList")
        self.formatList.addItem("")
        self.formatList.addItem("")
        self.formatList.addItem("")
        self.horizontalLayout.addWidget(self.formatList)
        self.convertButton = QtWidgets.QPushButton(Window)
        self.convertButton.setMinimumSize(QtCore.QSize(0, 30))
        self.convertButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.convertButton.setObjectName("convertButton")
        self.horizontalLayout.addWidget(self.convertButton)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.progressBar = QtWidgets.QProgressBar(Window)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 2)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "PyFFMPEGui"))
        self.label.setText(_translate("Window", "Source Directory:"))
        self.loadFilesButton.setText(_translate("Window", "&Load Files"))
        self.label_2.setText(_translate("Window", "Files to Convert"))
        self.label_3.setText(_translate("Window", "Converted"))
        self.label_4.setText(_translate("Window", "Convert to:"))
        self.formatList.setItemText(0, _translate("Window", "mp4"))
        self.formatList.setItemText(1, _translate("Window", "mkv"))
        self.formatList.setItemText(2, _translate("Window", "gif"))
        self.convertButton.setText(_translate("Window", "&Convert"))