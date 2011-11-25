#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_newrecord import Ui_NewRecordWindow

class EHRNewRecordWindow(QtGui.QDialog, Ui_NewRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Set today's date for first visit
        self.labelFirstVisit.setText(QtCore.QDate.currentDate().toString(QtCore.Qt.ISODate))

    def saveRecord(self):
        # Saves the record into the database
        pass
