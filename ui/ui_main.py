# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Thu Nov 24 16:27:31 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

import gettext
__trans = gettext.translation('ehr', fallback=True)
i18n = __trans.ugettext
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EHRMainWindow(object):
    def setupUi(self, EHRMainWindow):
        EHRMainWindow.setObjectName(_fromUtf8("EHRMainWindow"))
        EHRMainWindow.resize(600, 136)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EHRMainWindow.sizePolicy().hasHeightForWidth())
        EHRMainWindow.setSizePolicy(sizePolicy)
        EHRMainWindow.setMinimumSize(QtCore.QSize(600, 136))
        EHRMainWindow.setMaximumSize(QtCore.QSize(600, 136))
        EHRMainWindow.setWindowTitle(i18n("EHR"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Health.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EHRMainWindow.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(EHRMainWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(EHRMainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(128, 128))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Health.png")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 3, 1)
        self.label_2 = QtGui.QLabel(EHRMainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setText(i18n("Elektronik Sağlık Kayıt Sistemi"))
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(EHRMainWindow)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setText(i18n("Ozan Çağlayan"))
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButtonNewRecord = QtGui.QPushButton(EHRMainWindow)
        self.pushButtonNewRecord.setText(i18n("Yeni Kayıt"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/address-book-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonNewRecord.setIcon(icon1)
        self.pushButtonNewRecord.setObjectName(_fromUtf8("pushButtonNewRecord"))
        self.horizontalLayout_2.addWidget(self.pushButtonNewRecord)
        self.pushButtonSearchRecord = QtGui.QPushButton(EHRMainWindow)
        self.pushButtonSearchRecord.setText(i18n("Kayıt Ara"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/system-search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSearchRecord.setIcon(icon2)
        self.pushButtonSearchRecord.setObjectName(_fromUtf8("pushButtonSearchRecord"))
        self.horizontalLayout_2.addWidget(self.pushButtonSearchRecord)
        self.pushButtonExit = QtGui.QPushButton(EHRMainWindow)
        self.pushButtonExit.setText(i18n("Çıkış"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonExit.setIcon(icon3)
        self.pushButtonExit.setObjectName(_fromUtf8("pushButtonExit"))
        self.horizontalLayout_2.addWidget(self.pushButtonExit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.retranslateUi(EHRMainWindow)
        QtCore.QMetaObject.connectSlotsByName(EHRMainWindow)

    def retranslateUi(self, EHRMainWindow):
        pass

import icons_rc
import icons_rc
