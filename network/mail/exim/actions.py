#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt
import shutil
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("USER","q")

def setup():
    shutil.copy("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/src/EDITME","/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile")
    shutil.copy("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/exim_monitor/EDITME","/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/eximon.conf")   
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/usr/exim/bin","/usr/bin")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/usr/exim/configure","/etc/exim.conf")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/src/buildconfig.c","EXIM_USER","USER")
    pisitools.dosed("/var/pisi/exim-4.80.1-1/work/exim-4.80.1/Local/Makefile","/var/spool/exim","/var/pisi/exim-4.80.1-1/install/var/spool/exim")
    
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
 