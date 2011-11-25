#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_newrecord import Ui_NewRecordWindow

class EHRNewRecordWindow(QtGui.QDialog, Ui_NewRecordWindow):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Set today's date for first visit
        self.labelFirstVisit.setText(QtCore.QDate.currentDate().toString(QtCore.Qt.ISODate))

        # Connect the close button
        self.pushButtonClose.clicked.connect(self.hide)
        self.pushButtonSave.clicked.connect(self.saveRecord)

        # Connect DICOM buttons
        self.pushButtonAddDICOM.clicked.connect(self.slotShowDICOMFileBrowser)
        self.pushButtonRemoveDICOM.clicked.connect(self.slotRemoveSelectedDICOMFiles)

        self.listWidgetDICOM.itemDoubleClicked.connect(self.slotShowDICOMImage)

        self.dicomFiles = {}

    def getDiseases(self):
        diseases = []
        selectedListWidget = self.kactionselectorICD.selectedListWidget()
        for index in xrange(selectedListWidget.count()):
            diseases.append(unicode(selectedListWidget.item(index).text()))

        return "\n".join(diseases)

    def getDrugs(self):
        drugs = []
        selectedListWidget = self.kactionselectorDrugs.selectedListWidget()
        for index in xrange(selectedListWidget.count()):
            drugs.append(unicode(selectedListWidget.item(index).text()))

        return "\n".join(drugs)

    def slotRemoveSelectedDICOMFiles(self):
        for dicomFile in self.listWidgetDICOM.selectedItems():
            self.listWidgetDICOM.takeItem(self.listWidgetDICOM.row(dicomFile))

    def slotShowDICOMImage(self, item):
        os.system("gdcmviewer '%s'" % item.data(QtCore.Qt.UserRole).toString())


    def slotShowDICOMFileBrowser(self):
        fileDialog = QtGui.QFileDialog(self, unicode("DICOM dizini seçin..."),
                                       os.path.expanduser("~"),
                                       unicode("DICOM Dosyaları (*.dcm)"))
        fileDialog.setFileMode(QtGui.QFileDialog.ExistingFiles)

        if fileDialog.exec_():
            fileDialog.selectedFiles().clear()
            #self.listWidgetDICOM.addItems(fileDialog.selectedFiles())
            for file_ in fileDialog.selectedFiles():
                item = QtGui.QListWidgetItem(os.path.basename(unicode(file_)), self.listWidgetDICOM)
                item.setData(QtCore.Qt.UserRole, unicode(file_))






    def saveRecord(self):
        # FIXME: Check for empty fields
        # Saves the record into the database
        d = {"firstName"    : unicode(self.lineEditFirstName.text()),
             "lastName"     : unicode(self.lineEditLastName.text()),
             "birthPlace"   : unicode(self.lineEditBirthPlace.text()),
             "birthDate"    : unicode(self.dateEditBirthDate.date().toString(QtCore.Qt.ISODate)),
             "sex"          : unicode(self.comboBoxSex.currentText()),
             "maritalStatus": unicode(self.comboBoxMaritalStatus.currentText()),
             "occupation"   : unicode(self.comboBoxOccupation.currentText()),
             "sgkno"        : unicode(self.lineEditSGKNo.text()),
             "drink"        : unicode(self.comboBoxSmoke.currentText()),
             "smoke"        : unicode(self.comboBoxDrink.currentText()),
             "address"      : unicode(self.plainTextEditAddress.toPlainText()),
             "phone"        : unicode(self.lineEditPhoneNumber.text()),
             "photo"        : unicode("NONE"),
             "firstVisit"   : unicode(self.labelFirstVisit.text()),
             "email"        : unicode(self.lineEditEmail.text()),
             "history"      : unicode(self.plainTextEditStory.toPlainText()),
             "diagnostics"  : unicode(self.plainTextEditDiagnostics.toPlainText()),
             "diseases"     : unicode(self.getDiseases()),
             "drugs"        : unicode(self.getDrugs()),
             "drugNotes"    : unicode(self.plainTextEditDrugNotes.toPlainText())}

        retval = self.parent().dbManager.insertNewRecord(d)

        if retval:
            QtGui.QMessageBox.information(self, unicode("Kayıt Bilgisi"), "<b>%s %s</b> başarıyla kaydedildi." % (d['firstName'], d['lastName']))
            self.pushButtonSave.setText(unicode("Güncelle"))
        else:
            QtGui.QMessageBox.critical(self, unicode("Kayıt Bilgisi"), "<b>%s %s</b> kaydedilemedi. Lütfen tekrar deneyin." % (d['firstName'], d['lastName']))

