#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_main import Ui_EHRMainWindow

from ehrnewrecordwindow import EHRNewRecordWindow
from ehrsearchrecordwindow import EHRSearchRecordWindow

from ehrdbmanager import EHRDBManager

import cPickle

class EHR(QtGui.QDialog, Ui_EHRMainWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        self.searchRecordWindow = EHRSearchRecordWindow(self)

        self.dbManager = EHRDBManager()
        if not self.dbManager.open():
            # FIXME: DB problem, messagebox
            print "db problem"

        # Load drugs and diseases now for speed-up
        self.drugs = [unicode(f) for f in cPickle.load(open("data/drugs.db", "r"))]
        self.icd10 = [unicode("%s:%s" % (k,v)) for k,v in cPickle.load(open("data/icd10.db", "r")).items()]

        # Connect signals for buttons
        self.pushButtonNewRecord.clicked.connect(self.createNewRecordWindow)
        self.pushButtonSearchRecord.clicked.connect(self.searchRecordWindow.show)
        self.pushButtonExit.clicked.connect(QtGui.qApp.quit)


    def createNewRecordWindow(self):
        self.newRecordWindow = EHRNewRecordWindow(self)

        self.newRecordWindow.kactionselectorDrugs.availableListWidget().addItems(self.drugs)
        self.newRecordWindow.kactionselectorICD.availableListWidget().addItems(sorted(self.icd10))

        self.newRecordWindow.show()


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    ehr = EHR()
    ehr.show()

    app.exec_()
