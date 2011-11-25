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
'%(photo)s',
'%(firstVisit)s',
'%(email)s',
'%(history)s',
'%(diseases)s',
'%(drugs)s',
'%(drugNotes)s')"""


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
        return query.exec_(self.insert_query % data_dict)

    def updateRecord(self, data_dict):
        pass

    def searchRecord(self, data_dict):
        pass
