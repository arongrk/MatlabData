from ctypes import c_int32
import struct

MARKER = c_int32(0xaaffffff).value
PACKAGE_LENGTH = 350
PLOT_LENGTH = 40960
IP_Address = '192.168.1.1'
PORT = 9090

MARKER_BYTES = struct.pack('!i', MARKER)
PACKAGE_SIZE = PACKAGE_LENGTH * 4
PLOT_SIZE = PLOT_LENGTH * 4
# PACKAGE_LENGTH = 3
# PLOT_LENGTH = 7
