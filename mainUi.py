# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Oct 07 00:59:47 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(520, 290)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(520, 290))
        MainWindow.setMaximumSize(QtCore.QSize(520, 290))
        MainWindow.setStyleSheet(_fromUtf8("background: rgb(52, 52, 52)"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(_fromUtf8("color: #FFF;\n"
""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.change = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setStyleSheet(_fromUtf8("background: rgb(76, 76, 76);"))
        self.change.setFrameShape(QtGui.QFrame.NoFrame)
        self.change.setScaledContents(False)
        self.change.setAlignment(QtCore.Qt.AlignCenter)
        self.change.setObjectName(_fromUtf8("change"))
        self.verticalLayout.addWidget(self.change)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet(_fromUtf8("border: #FFF;\n"
"background: rgb(76, 76, 76);"))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.ratingTotal = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ratingTotal.setFont(font)
        self.ratingTotal.setStyleSheet(_fromUtf8("color: #00FF00;"))
        self.ratingTotal.setAlignment(QtCore.Qt.AlignCenter)
        self.ratingTotal.setObjectName(_fromUtf8("ratingTotal"))
        self.horizontalLayout_8.addWidget(self.ratingTotal)
        self.ratingSession = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.ratingSession.setFont(font)
        self.ratingSession.setStyleSheet(_fromUtf8("color: rgb(170, 85, 255)"))
        self.ratingSession.setAlignment(QtCore.Qt.AlignCenter)
        self.ratingSession.setObjectName(_fromUtf8("ratingSession"))
        self.horizontalLayout_8.addWidget(self.ratingSession)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        spacerItem1 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet(_fromUtf8("border: #FFF;\n"
"background: rgb(76, 76, 76);"))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.fragsAvg = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.fragsAvg.setFont(font)
        self.fragsAvg.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.fragsAvg.setFrameShape(QtGui.QFrame.NoFrame)
        self.fragsAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.fragsAvg.setObjectName(_fromUtf8("fragsAvg"))
        self.horizontalLayout_4.addWidget(self.fragsAvg)
        spacerItem3 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.fragsChange = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.fragsChange.setFont(font)
        self.fragsChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.fragsChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.fragsChange.setAlignment(QtCore.Qt.AlignCenter)
        self.fragsChange.setObjectName(_fromUtf8("fragsChange"))
        self.horizontalLayout_4.addWidget(self.fragsChange)
        self.horizontalLayout.addLayout(self.horizontalLayout_4)
        spacerItem4 = QtGui.QSpacerItem(15, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.dmgAvg = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.dmgAvg.setFont(font)
        self.dmgAvg.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.dmgAvg.setFrameShape(QtGui.QFrame.NoFrame)
        self.dmgAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.dmgAvg.setObjectName(_fromUtf8("dmgAvg"))
        self.horizontalLayout_2.addWidget(self.dmgAvg)
        spacerItem5 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.dmgChange = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.dmgChange.setFont(font)
        self.dmgChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.dmgChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.dmgChange.setAlignment(QtCore.Qt.AlignCenter)
        self.dmgChange.setObjectName(_fromUtf8("dmgChange"))
        self.horizontalLayout_2.addWidget(self.dmgChange)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtGui.QSpacerItem(15, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.spotAvg = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.spotAvg.setFont(font)
        self.spotAvg.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.spotAvg.setFrameShape(QtGui.QFrame.NoFrame)
        self.spotAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.spotAvg.setObjectName(_fromUtf8("spotAvg"))
        self.horizontalLayout_3.addWidget(self.spotAvg)
        spacerItem7 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.spotChange = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.spotChange.setFont(font)
        self.spotChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.spotChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.spotChange.setAlignment(QtCore.Qt.AlignCenter)
        self.spotChange.setObjectName(_fromUtf8("spotChange"))
        self.horizontalLayout_3.addWidget(self.spotChange)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        spacerItem8 = QtGui.QSpacerItem(15, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.defAvg = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.defAvg.setFont(font)
        self.defAvg.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.defAvg.setFrameShape(QtGui.QFrame.NoFrame)
        self.defAvg.setAlignment(QtCore.Qt.AlignCenter)
        self.defAvg.setObjectName(_fromUtf8("defAvg"))
        self.horizontalLayout_5.addWidget(self.defAvg)
        spacerItem9 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.defChange = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.defChange.setFont(font)
        self.defChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.defChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.defChange.setAlignment(QtCore.Qt.AlignCenter)
        self.defChange.setObjectName(_fromUtf8("defChange"))
        self.horizontalLayout_5.addWidget(self.defChange)
        self.horizontalLayout.addLayout(self.horizontalLayout_5)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem11 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem11)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet(_fromUtf8("border: #FFF;\n"
"background: rgb(76, 76, 76);"))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.battleSession = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.battleSession.setFont(font)
        self.battleSession.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.battleSession.setFrameShape(QtGui.QFrame.NoFrame)
        self.battleSession.setAlignment(QtCore.Qt.AlignCenter)
        self.battleSession.setObjectName(_fromUtf8("battleSession"))
        self.horizontalLayout_7.addWidget(self.battleSession)
        spacerItem13 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.winSession = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.winSession.setFont(font)
        self.winSession.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.winSession.setFrameShape(QtGui.QFrame.NoFrame)
        self.winSession.setAlignment(QtCore.Qt.AlignCenter)
        self.winSession.setObjectName(_fromUtf8("winSession"))
        self.horizontalLayout_7.addWidget(self.winSession)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        spacerItem14 = QtGui.QSpacerItem(15, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem14)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.wrSession = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.wrSession.setFont(font)
        self.wrSession.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.wrSession.setFrameShape(QtGui.QFrame.NoFrame)
        self.wrSession.setAlignment(QtCore.Qt.AlignCenter)
        self.wrSession.setObjectName(_fromUtf8("wrSession"))
        self.horizontalLayout_9.addWidget(self.wrSession)
        spacerItem15 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.wrChange = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.wrChange.setFont(font)
        self.wrChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.wrChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.wrChange.setAlignment(QtCore.Qt.AlignCenter)
        self.wrChange.setObjectName(_fromUtf8("wrChange"))
        self.horizontalLayout_9.addWidget(self.wrChange)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        spacerItem16 = QtGui.QSpacerItem(15, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tierSession = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tierSession.setFont(font)
        self.tierSession.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.tierSession.setFrameShape(QtGui.QFrame.NoFrame)
        self.tierSession.setAlignment(QtCore.Qt.AlignCenter)
        self.tierSession.setObjectName(_fromUtf8("tierSession"))
        self.horizontalLayout_6.addWidget(self.tierSession)
        spacerItem17 = QtGui.QSpacerItem(5, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17)
        self.tierChange = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.tierChange.setFont(font)
        self.tierChange.setStyleSheet(_fromUtf8("border: none; background: none;"))
        self.tierChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.tierChange.setAlignment(QtCore.Qt.AlignCenter)
        self.tierChange.setObjectName(_fromUtf8("tierChange"))
        self.horizontalLayout_6.addWidget(self.tierChange)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        spacerItem18 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        spacerItem19 = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.lastToggle = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Trebuchet MS"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lastToggle.setFont(font)
        self.lastToggle.setStyleSheet(_fromUtf8("border: #FFF;\n"
"background: rgb(40,63, 83);\n"
"padding: 5px;"))
        self.lastToggle.setObjectName(_fromUtf8("lastToggle"))
        self.verticalLayout_2.addWidget(self.lastToggle)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.change.setText(_translate("MainWindow", "+1.743", None))
        self.ratingTotal.setText(_translate("MainWindow", "1527.23", None))
        self.ratingSession.setText(_translate("MainWindow", "2000.01", None))
        self.fragsAvg.setText(_translate("MainWindow", "0.00", None))
        self.fragsChange.setText(_translate("MainWindow", "1.34", None))
        self.dmgAvg.setText(_translate("MainWindow", "0.00", None))
        self.dmgChange.setText(_translate("MainWindow", "1.34", None))
        self.spotAvg.setText(_translate("MainWindow", "0.00", None))
        self.spotChange.setText(_translate("MainWindow", "1.34", None))
        self.defAvg.setText(_translate("MainWindow", "0.00", None))
        self.defChange.setText(_translate("MainWindow", "1.34", None))
        self.battleSession.setText(_translate("MainWindow", "0.00", None))
        self.winSession.setText(_translate("MainWindow", "1.34", None))
        self.wrSession.setText(_translate("MainWindow", "0.00", None))
        self.wrChange.setText(_translate("MainWindow", "1.34", None))
        self.tierSession.setText(_translate("MainWindow", "0.00", None))
        self.tierChange.setText(_translate("MainWindow", "1.34", None))
        self.lastToggle.setText(_translate("MainWindow", "LAST", None))
