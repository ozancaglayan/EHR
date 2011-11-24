#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_searchrecord import Ui_SearchRecordWindow

class EHRSearchRecordWindow(QtGui.QDialog, Ui_SearchRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Sİnyalleri filan burda bagla
