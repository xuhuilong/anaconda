# bar.py
# Example DBUS module
#
# Copyright (C) 2017 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#

from pyanaconda.dbus import dbus_constants
from pyanaconda.modules.base import BaseModule
from pyanaconda.dbus.interface import dbus_interface
from pyanaconda.dbus.typing import *  # pylint: disable=wildcard-import

from pyanaconda import anaconda_logging
log = anaconda_logging.get_dbus_module_logger(__name__)

@dbus_interface(dbus_constants.ADDON_BAZ)
class Baz(BaseModule):

    def __init__(self):
        super().__init__()
        self._dbus_name = dbus_constants.ADDON_BAZ

    def EchoString(self, s: Str) -> Str:
        """Returns whatever is passed to it."""
        log.debug(s)
        return s
