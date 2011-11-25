#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_searchrecord import Ui_SearchRecordWindow

class EHRSearchRecordWindow(QtGui.QDialog, Ui_SearchRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Signal/Slot stuff
        self.pushButtonCloseSearch.clicked.connect(self.hide)
        self.lineEditSearch.textChanged.connect(self.searchRecord)


    def searchRecord(self):
        self.treeWidgetSearch.clear()

        term = self.lineEditSearch.text()
        searchResult = self.parent().dbManager.searchRecord(term, term)

        result = QtGui.QTreeWidgetItem(self.treeWidgetSearch)

        for i, column in enumerate(searchResult):
            result.setText(i, column)
