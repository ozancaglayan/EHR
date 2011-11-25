#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class EHRDBManager(object):
    def __init__(self):
        self.db_name = os.path.expanduser("~/.ehr.sqlite")


    def inserNewRecord(self):
        pass

    def updateRecord(self, id_):
        pass

    def searchRecord(self, data):
        pass
