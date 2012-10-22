#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyleft 2012 Pardus ANKA Community
# Copyright 2005-2011 TUBITAK/UEAKE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#from pisi.actionsapi import autotools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    #for i in shelltools.ls("."):
        #if shelltools.isDirectory(i) and shelltools.isFile("%s/Makefile.am" % i):
            #pisitools.dosed("%s/Makefile.am" % i, "-Werror")

    #autotools.autoreconf("-fi")

    #Do not create pyo/pyc
    #pisitools.dosed("wrapper/Makefile.in", "^py_compile.*=.*", "py_compile = /bin/true")

    #autotools.configure("--enable-python --disable-debug --enable-engine --enable-tools")

    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON")

def build():
    #autotools.make()
    cmaketools.make()

def install():
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "AUTHORS")
