#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def build():
    # we do have r49539, setup.cfg and setup.py are wrong
    pisitools.dosed("setup.*", "49539", "0")
    pythonmodules.compile()

def install():
    pythonmodules.install()
