#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.ui_newrecord import Ui_NewRecordWindow

class EHRNewRecordWindow(QtGui.QDialog, Ui_NewRecordWindow):
    def __init__(self, parent=None, id_=None):
        QtGui.QDialog.__init__(self, parent)

        self.setupUi(self)

        # Connect the close button
        self.pushButtonClose.clicked.connect(self.hide)
        self.pushButtonSave.clicked.connect(self.saveRecord)

        # Photo
        self.pushButtonAddPhoto.clicked.connect(self.slotShowPhotoBrowser)

        # Connect DICOM buttons
        self.pushButtonAddDICOM.clicked.connect(self.slotShowDICOMFileBrowser)
        self.pushButtonRemoveDICOM.clicked.connect(self.slotRemoveSelectedDICOMFiles)
        self.listWidgetDICOM.itemDoubleClicked.connect(self.slotShowDICOMImage)

        # New or show record window?
        if id_:
            # We'll show existing record
            result = self.parent().parent().dbManager.getRecord(id_)

            self.kactionselectorDrugs.availableListWidget().addItems(self.parent().parent().drugs)
            self.kactionselectorICD.availableListWidget().addItems(sorted(self.parent().parent().icd10))

            if result:
                self.lineEditFirstName.setText(result[0])
                self.lineEditLastName.setText(result[1])
                self.lineEditBirthPlace.setText(result[2])
                self.dateEditBirthDate.setDate(QtCore.QDate.fromString(result[3], QtCore.Qt.ISODate))
                self.comboBoxSex.setCurrentIndex(self.comboBoxSex.findText(result[4]))
                self.comboBoxMaritalStatus.setCurrentIndex(self.comboBoxMaritalStatus.findText(result[5]))
                self.comboBoxOccupation.setCurrentIndex(self.comboBoxOccupation.findText(result[6]))
                self.lineEditSGKNo.setText(result[7])
                self.comboBoxSmoke.setCurrentIndex(self.comboBoxSmoke.findText(result[8]))
                self.comboBoxDrink.setCurrentIndex(self.comboBoxDrink.findText(result[9]))
                self.plainTextEditAddress.setPlainText(result[10])
                self.lineEditPhoneNumber.setText(result[11])
                #self.labelPhoto.setPixmap(QtGui.QPixmap(result[12].data()))
                self.labelFirstVisit.setText(result[13])
                self.lineEditEmail.setText(result[14])
                self.plainTextEditStory.setPlainText(result[15])
                self.plainTextEditDiagnostics.setPlainText(result[16])
                self.setDiseases(result[17])
                self.setDrugs(result[18])
                self.plainTextEditDrugNotes.setPlainText(result[19])

        else:
            # Set today's date for first visit
            self.labelFirstVisit.setText(QtCore.QDate.currentDate().toString(QtCore.Qt.ISODate))

    def getDiseases(self):
        diseases = []
        selectedListWidget = self.kactionselectorICD.selectedListWidget()
        for index in xrange(selectedListWidget.count()):
            diseases.append(unicode(selectedListWidget.item(index).text()))

        return "\n".join(diseases)

    def setDiseases(self, diseases):
        for disease in diseases.split("\n"):
            self.kactionselectorICD.selectedListWidget().addItem(disease)

    def getDrugs(self):
        drugs = []
        selectedListWidget = self.kactionselectorDrugs.selectedListWidget()
        for index in xrange(selectedListWidget.count()):
            drugs.append(unicode(selectedListWidget.item(index).text()))

        return "\n".join(drugs)

    def setDrugs(self, drugs):
        for drug in drugs.split("\n"):
            self.kactionselectorDrugs.selectedListWidget().addItem(drug)

    def slotRemoveSelectedDICOMFiles(self):
        for dicomFile in self.listWidgetDICOM.selectedItems():
            self.listWidgetDICOM.takeItem(self.listWidgetDICOM.row(dicomFile))

    def slotShowDICOMImage(self, item):
        import vtk
        reader = vtk.vtkDICOMImageReader()
        dicom_file = unicode(item.data(QtCore.Qt.UserRole).toString())
        reader.SetFileName(dicom_file)
        reader.Update()

        imageViewer = vtk.vtkImageViewer()
        imageViewer.SetInputConnection(reader.GetOutputPort())

        self.qvtkWidget.SetRenderWindow(imageViewer.GetRenderWindow())
        imageViewer.SetupInteractor(self.qvtkWidget.GetRenderWindow().GetInteractor())

        imageViewer.SetColorLevel(128)
        imageViewer.SetColorWindow(256)
        imageViewer.SetSize(self.qvtkWidget.geometry().width(), self.qvtkWidget.geometry().height())
        #os.system("gdcmviewer '%s'" % item.data(QtCore.Qt.UserRole).toString())


    def slotShowDICOMFileBrowser(self):
        fileDialog = QtGui.QFileDialog(self, unicode("DICOM dizini seçin..."),
                                       os.path.expanduser("~"),
                                       unicode("DICOM Dosyaları (*.dcm)"))
        fileDialog.setFileMode(QtGui.QFileDialog.ExistingFiles)

        if fileDialog.exec_():
            fileDialog.selectedFiles().clear()
            for file_ in fileDialog.selectedFiles():
                item = QtGui.QListWidgetItem(os.path.basename(unicode(file_)), self.listWidgetDICOM)
                item.setData(QtCore.Qt.UserRole, unicode(file_))

    def slotShowPhotoBrowser(self):
            fileDialog = QtGui.QFileDialog(self, unicode("Bir Fotoğraf Seçin..."),
                                           os.path.expanduser("~"),
                                           unicode("Görüntü Dosyaları (*.jpg *.jpeg *.png *.bmp)"))
            fileDialog.setFileMode(QtGui.QFileDialog.ExistingFile)

            if fileDialog.exec_():
                fileDialog.selectedFiles().clear()
                pixmap = QtGui.QPixmap(fileDialog.selectedFiles()[0])
                #pixmap = pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
                self.labelPhoto.setPixmap(pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio))


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
             "photo"        : self.labelPhoto.pixmap(),
             "firstVisit"   : unicode(self.labelFirstVisit.text()),
             "email"        : unicode(self.lineEditEmail.text()),
             "history"      : unicode(self.plainTextEditStory.toPlainText()),
             "diagnostics"  : unicode(self.plainTextEditDiagnostics.toPlainText()),
             "diseases"     : unicode(self.getDiseases()),
             "drugs"        : unicode(self.getDrugs()),
             "drugNotes"    : unicode(self.plainTextEditDrugNotes.toPlainText())}

        if self.labelPhoto.pixmap():
            print self.labelPhoto.pixmap()

        retval = self.parent().dbManager.insertNewRecord(d)

        if retval:
            QtGui.QMessageBox.information(self, unicode("Kayıt Bilgisi"), "<b>%s %s</b> başarıyla kaydedildi." % (d['firstName'], d['lastName']))
            #self.pushButtonSave.setText(unicode("Güncelle"))
        else:
            QtGui.QMessageBox.critical(self, unicode("Kayıt Bilgisi"), "<b>%s %s</b> kaydedilemedi. Lütfen tekrar deneyin." % (d['firstName'], d['lastName']))

