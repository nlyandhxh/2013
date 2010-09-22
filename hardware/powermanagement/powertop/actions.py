#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed('Makefile', 'CFLAGS\?=.*', 'CFLAGS=%s' % get.CFLAGS())
    pisitools.dosed('Makefile', 'CC\?=.*', 'CC=%s' % get.CC())

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR=%s' % get.installDIR())

    pisitools.dodoc('COPYING', 'Changelog', 'README')
