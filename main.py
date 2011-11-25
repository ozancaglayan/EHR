#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_main import Ui_EHRMainWindow

from ehrnewrecordwindow import EHRNewRecordWindow
from ehrsearchrecordwindow import EHRSearchRecordWindow

import cPickle

class EHR(QtGui.QDialog, Ui_EHRMainWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        self.newRecordWindow = EHRNewRecordWindow(self)
        self.searchRecordWindow = EHRSearchRecordWindow(self)

        # Load drugs and diseases now for speed-up
        self.drugs = [unicode(f) for f in cPickle.load(open("data/drugs.db", "r"))]
        self.icd10 = [unicode("%s:%s" % (k,v)) for k,v in cPickle.load(open("data/icd10.db", "r")).items()]
        self.newRecordWindow.kactionselectorDrugs.availableListWidget().addItems(self.drugs)
        self.newRecordWindow.kactionselectorICD.availableListWidget().addItems(sorted(self.icd10))

        # Connect signals for buttons
        self.pushButtonNewRecord.clicked.connect(self.newRecordWindow.show)
        self.pushButtonSearchRecord.clicked.connect(self.searchRecordWindow.show)
        self.pushButtonExit.clicked.connect(QtGui.qApp.quit)


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    ehr = EHR()
    ehr.show()

    app.exec_()
