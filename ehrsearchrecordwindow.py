#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_searchrecord import Ui_SearchRecordWindow

from ehrnewrecordwindow import EHRNewRecordWindow

class EHRSearchRecordWindow(QtGui.QDialog, Ui_SearchRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Signal/Slot stuff
        self.pushButtonCloseSearch.clicked.connect(self.hide)
        self.lineEditSearch.textChanged.connect(self.searchRecord)
        self.treeWidgetSearch.itemDoubleClicked.connect(self.showRecord)

        # Trigger it initially for filling the results
        self.searchRecord()

    def showRecord(self, item, column):
        showRecordWindow = EHRNewRecordWindow(self, item.text(0))
        self.hide()
        showRecordWindow.show()

    def searchRecord(self):
        self.treeWidgetSearch.clear()

        term = self.lineEditSearch.text()
        searchResults = self.parent().dbManager.searchRecord(term, term)

        for searchResult in searchResults:
            result = QtGui.QTreeWidgetItem(self.treeWidgetSearch)

            for i, column in enumerate(searchResult):
                result.setText(i, column)

            del result
