#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_main import Ui_EHRMainWindow
from ui.ui_newrecord import Ui_NewRecordWindow

class EHRNewRecordWindow(QtGui.QDialog, Ui_NewRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Sİnyalleri filan burda bagla



class EHR(QtGui.QDialog, Ui_EHRMainWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        self.newRecordWindow = EHRNewRecordWindow(self)

        self.pushButtonNewRecord.clicked.connect(self.newRecordWindow.show)
        self.pushButtonExit.clicked.connect(QtGui.qApp.quit)

        # self.pushButton2 ile erişiriz




if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    ehr = EHR()
    ehr.show()

    app.exec_()
