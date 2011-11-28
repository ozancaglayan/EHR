#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from PyQt4.QtSql import QSqlDatabase, QSqlQuery

class EHRDBManager(object):
    def __init__(self):
        self.db_path = os.path.expanduser("~/.ehr.sqlite")
        self.available = os.path.exists(self.db_path)

        self.handle = QSqlDatabase.addDatabase("QSQLITE")
        self.handle.setDatabaseName(self.db_path)

        self.init_query = """
CREATE TABLE records (id integer primary key,
firstname varchar(30),
lastname varchar(30),
birthplace varchar(30),
birthdate datetime,
sex nchar(1),
marital varchar(10),
occupation varchar(30),
sgkno varchar(20),
drink varchar(30),
smoke varchar(30),
address varchar(200),
phone varchar(15),
photo blob,
firstvisit datetime,
email varchar(40),
history text,
diseases text,
dicoms text,
diagnostics text,
drugs text,
drugnotes text)"""

        self.insert_query = """
INSERT INTO records VALUES(NULL,
'%(firstName)s',
'%(lastName)s',
'%(birthPlace)s',
'%(birthDate)s',
'%(sex)s',
'%(maritalStatus)s',
'%(occupation)s',
'%(sgkno)s',
'%(drink)s',
'%(smoke)s',
'%(address)s',
'%(phone)s',
:photo,
'%(firstVisit)s',
'%(email)s',
'%(history)s',
'%(diseases)s',
'%(dicoms)s',
'%(diagnostics)s',
'%(drugs)s',
'%(drugNotes)s')"""

        self.update_query = """
UPDATE records
SET firstname='%(firstName)s',
lastname='%(lastName)s',
birthplace='%(birthPlace)s',
birthdate='%(birthDate)s',
sex='%(sex)s',
marital='%(maritalStatus)s',
occupation='%(occupation)s',
sgkno='%(sgkno)s',
drink='%(drink)s',
smoke='%(smoke)s',
address='%(address)s',
phone='%(phone)s',
photo=:photo,
email='%(email)s',
history='%(history)s',
diseases='%(diseases)s',
dicoms='%(dicoms)s',
diagnostics='%(diagnostics)s',
drugs='%(drugs)s',
drugnotes='%(drugNotes)s'
WHERE id='%(id_)s'"""

        self.search_query = """
SELECT id,firstname,lastname,sex,firstvisit,phone FROM records WHERE firstname LIKE '%%%s%%' OR
lastname LIKE '%%%s%%'"""

        self.fetch_query = """
SELECT * FROM records WHERE id='%s'"""


    def open(self):
        retval = self.handle.open()

        if retval:
            # Check whether the DB contains our table if not
            # initialize it.
            if len(self.handle.tables()) == 0:
                # Create it
                query = QSqlQuery(self.handle)
                return query.exec_(self.init_query)

        return retval

    def insertNewRecord(self, data_dict):
        query = QSqlQuery(self.handle)
        if query.prepare(self.insert_query % data_dict):
            query.bindValue(":photo", data_dict['photo'])
            return query.exec_()
        else:
            return False

    def updateRecord(self, id_, data_dict):
        # Register id too
        data_dict['id_'] = id_

        # Prepare query
        query = QSqlQuery(self.handle)

        if query.prepare(self.update_query % data_dict):
            query.bindValue(":photo", data_dict['photo'])
            return query.exec_()
        else:
            return False

    def getRecord(self, id_):
        query = QSqlQuery(self.handle)
        query.exec_(self.fetch_query % id_)

        result = None

        while query.next():
            # 22: number of total fields, skip first id field
            result = [query.value(i).toString() for i in range(1,22)]
            result[12] = query.value(13).toByteArray()

        return result

    def searchRecord(self, firstName, lastName):
        query = QSqlQuery(self.handle)
        retval = query.exec_(self.search_query % (firstName, lastName))

        results = []

        while query.next():
            result = [query.value(i).toString() for i in range(6)]
            results.append(result)

        return results
