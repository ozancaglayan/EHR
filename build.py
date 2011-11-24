#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

for ui in glob.glob1("ui", "*.ui"):
    os.system("/usr/bin/pyuic4 -o ui/ui_%s.py ui/%s -g ehr" % (ui.split(".")[0], ui))

os.system("pyrcc4 data/icons.qrc -o icons_rc.py")
